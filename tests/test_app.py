import io
from datetime import datetime
from social.app import App
from social.social_network import SocialNetwork


class FakeClock:
    def __init__(self):
        self._now = datetime(2025, 1, 15, 10, 0, 0)

    def now(self):
        return self._now

    def set(self, time):
        self._now = time


class TestApp:
    def _run_app(self, network, clock, commands):
        input_stream = io.StringIO("\n".join(commands) + "\n")
        output_stream = io.StringIO()
        app = App(network, clock, input_stream, output_stream)
        app.run()
        return output_stream.getvalue()

    def test_posting_and_reading(self):
        clock = FakeClock()
        network = SocialNetwork(clock)

        clock.set(datetime(2025, 1, 15, 9, 55, 0))
        network.post("Alice", "I love the weather today")
        clock.set(datetime(2025, 1, 15, 10, 0, 0))

        output = self._run_app(network, clock, ["Alice"])
        assert "I love the weather today (5 minutes ago)" in output

    def test_posting_via_command_and_reading(self):
        clock = FakeClock()
        network = SocialNetwork(clock)

        output = self._run_app(network, clock, [
            "Alice -> I love the weather today",
            "Alice",
        ])
        assert "I love the weather today (0 seconds ago)" in output

    def test_reading_scenario(self):
        """Bob's timeline shows posts in reverse chronological order."""
        clock = FakeClock()
        network = SocialNetwork(clock)

        clock.set(datetime(2025, 1, 15, 9, 58, 0))
        network.post("Bob", "Damn! We lost!")
        clock.set(datetime(2025, 1, 15, 9, 59, 0))
        network.post("Bob", "Good game though.")
        clock.set(datetime(2025, 1, 15, 10, 0, 0))

        output = self._run_app(network, clock, ["Bob"])
        good_pos = output.index("Good game though.")
        damn_pos = output.index("Damn! We lost!")
        assert good_pos < damn_pos

    def test_follow_and_wall(self):
        clock = FakeClock()
        network = SocialNetwork(clock)

        clock.set(datetime(2025, 1, 15, 9, 55, 0))
        network.post("Alice", "I love the weather today")
        clock.set(datetime(2025, 1, 15, 9, 58, 0))
        network.post("Bob", "Damn! We lost!")
        clock.set(datetime(2025, 1, 15, 9, 59, 0))
        network.post("Bob", "Good game though.")
        clock.set(datetime(2025, 1, 15, 9, 59, 45))
        network.post("Charlie", "I'm in New York today!")

        network.follow("Charlie", "Alice")
        network.follow("Charlie", "Bob")

        clock.set(datetime(2025, 1, 15, 10, 0, 0))
        output = self._run_app(network, clock, ["Charlie wall"])

        assert "Charlie - I'm in New York today!" in output
        assert "Bob - Good game though." in output
        assert "Bob - Damn! We lost!" in output
        assert "Alice - I love the weather today" in output

        # Check ordering
        charlie_pos = output.index("Charlie - I'm in New York today!")
        bob_good_pos = output.index("Bob - Good game though.")
        bob_damn_pos = output.index("Bob - Damn! We lost!")
        alice_pos = output.index("Alice - I love the weather today")
        assert charlie_pos < bob_good_pos < bob_damn_pos < alice_pos

    def test_full_scenario(self):
        """Test the complete scenario from the exercise description."""
        clock = FakeClock()
        network = SocialNetwork(clock)

        # Posting
        clock.set(datetime(2025, 1, 15, 9, 55, 0))
        network.post("Alice", "I love the weather today")
        clock.set(datetime(2025, 1, 15, 9, 58, 0))
        network.post("Bob", "Damn! We lost!")
        clock.set(datetime(2025, 1, 15, 9, 59, 0))
        network.post("Bob", "Good game though.")

        # Reading
        clock.set(datetime(2025, 1, 15, 10, 0, 0))
        output = self._run_app(network, clock, ["Alice"])
        assert "I love the weather today (5 minutes ago)" in output

        output = self._run_app(network, clock, ["Bob"])
        assert "Good game though. (1 minute ago)" in output
        assert "Damn! We lost! (2 minutes ago)" in output

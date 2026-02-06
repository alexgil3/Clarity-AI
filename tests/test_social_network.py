from datetime import datetime
from social.social_network import SocialNetwork


class FakeClock:
    def __init__(self):
        self._now = datetime(2025, 1, 15, 10, 0, 0)

    def now(self):
        return self._now

    def set(self, time):
        self._now = time


class TestPosting:
    def test_user_can_post_message(self):
        clock = FakeClock()
        network = SocialNetwork(clock)

        network.post("Alice", "I love the weather today")

        timeline = network.read("Alice")
        assert len(timeline) == 1
        assert timeline[0].message == "I love the weather today"
        assert timeline[0].username == "Alice"

    def test_user_can_post_multiple_messages(self):
        clock = FakeClock()
        network = SocialNetwork(clock)

        network.post("Bob", "Damn! We lost!")
        network.post("Bob", "Good game though.")

        timeline = network.read("Bob")
        assert len(timeline) == 2


class TestReading:
    def test_reading_unknown_user_returns_empty(self):
        clock = FakeClock()
        network = SocialNetwork(clock)

        timeline = network.read("Nobody")
        assert timeline == []

    def test_posts_appear_in_reverse_chronological_order(self):
        clock = FakeClock()
        network = SocialNetwork(clock)

        clock.set(datetime(2025, 1, 15, 10, 0, 0))
        network.post("Bob", "Damn! We lost!")
        clock.set(datetime(2025, 1, 15, 10, 1, 0))
        network.post("Bob", "Good game though.")

        timeline = network.read("Bob")
        assert timeline[0].message == "Good game though."
        assert timeline[1].message == "Damn! We lost!"

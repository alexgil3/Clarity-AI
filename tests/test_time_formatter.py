from datetime import datetime
from social.time_formatter import format_time


class TestTimeFormatter:
    def test_seconds_ago(self):
        now = datetime(2025, 1, 15, 10, 0, 30)
        timestamp = datetime(2025, 1, 15, 10, 0, 0)
        assert format_time(timestamp, now) == "30 seconds ago"

    def test_one_second_ago(self):
        now = datetime(2025, 1, 15, 10, 0, 1)
        timestamp = datetime(2025, 1, 15, 10, 0, 0)
        assert format_time(timestamp, now) == "1 second ago"

    def test_minutes_ago(self):
        now = datetime(2025, 1, 15, 10, 5, 0)
        timestamp = datetime(2025, 1, 15, 10, 0, 0)
        assert format_time(timestamp, now) == "5 minutes ago"

    def test_one_minute_ago(self):
        now = datetime(2025, 1, 15, 10, 1, 0)
        timestamp = datetime(2025, 1, 15, 10, 0, 0)
        assert format_time(timestamp, now) == "1 minute ago"

    def test_hours_ago(self):
        now = datetime(2025, 1, 15, 13, 0, 0)
        timestamp = datetime(2025, 1, 15, 10, 0, 0)
        assert format_time(timestamp, now) == "3 hours ago"

    def test_one_hour_ago(self):
        now = datetime(2025, 1, 15, 11, 0, 0)
        timestamp = datetime(2025, 1, 15, 10, 0, 0)
        assert format_time(timestamp, now) == "1 hour ago"

    def test_days_ago(self):
        now = datetime(2025, 1, 17, 10, 0, 0)
        timestamp = datetime(2025, 1, 15, 10, 0, 0)
        assert format_time(timestamp, now) == "2 days ago"

    def test_one_day_ago(self):
        now = datetime(2025, 1, 16, 10, 0, 0)
        timestamp = datetime(2025, 1, 15, 10, 0, 0)
        assert format_time(timestamp, now) == "1 day ago"

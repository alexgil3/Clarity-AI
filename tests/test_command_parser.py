from social.command_parser import (
    parse, PostCommand, ReadCommand, FollowCommand, WallCommand
)


class TestCommandParser:
    def test_parse_post_command(self):
        result = parse("Alice -> I love the weather today")
        assert result == PostCommand("Alice", "I love the weather today")

    def test_parse_read_command(self):
        result = parse("Alice")
        assert result == ReadCommand("Alice")

    def test_parse_follow_command(self):
        result = parse("Charlie follows Alice")
        assert result == FollowCommand("Charlie", "Alice")

    def test_parse_wall_command(self):
        result = parse("Charlie wall")
        assert result == WallCommand("Charlie")

    def test_post_with_arrow_in_message(self):
        result = parse("Alice -> look at this -> cool")
        assert result == PostCommand("Alice", "look at this -> cool")

    def test_ignores_leading_trailing_whitespace(self):
        result = parse("  Alice  ")
        assert result == ReadCommand("Alice")

    def test_unknown_command_returns_none(self):
        result = parse("Alice something weird here")
        assert result is None

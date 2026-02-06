import sys
from social.social_network import SocialNetwork
from social.command_parser import (
    parse, PostCommand, ReadCommand, FollowCommand, WallCommand
)
from social.time_formatter import format_time


class App:
    def __init__(self, social_network, clock, input_stream=None, output_stream=None):
        self.social_network = social_network
        self.clock = clock
        self.input = input_stream or sys.stdin
        self.output = output_stream or sys.stdout

    def run(self):
        while True:
            try:
                self.output.write("> ")
                self.output.flush()
                line = self.input.readline()
                if not line:
                    break
                line = line.strip()
                if not line:
                    continue
                self._handle(line)
            except (KeyboardInterrupt, EOFError):
                break

    def _handle(self, line):
        command = parse(line)

        if isinstance(command, PostCommand):
            self.social_network.post(command.username, command.message)

        elif isinstance(command, ReadCommand):
            posts = self.social_network.read(command.username)
            for post in posts:
                time_str = format_time(post.timestamp, self.clock.now())
                self.output.write(f"{post.message} ({time_str})\n")

        elif isinstance(command, FollowCommand):
            self.social_network.follow(command.username, command.target)

        elif isinstance(command, WallCommand):
            posts = self.social_network.wall(command.username)
            for post in posts:
                time_str = format_time(post.timestamp, self.clock.now())
                self.output.write(f"{post.username} - {post.message} ({time_str})\n")

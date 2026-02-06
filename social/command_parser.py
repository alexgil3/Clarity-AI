from collections import namedtuple

PostCommand = namedtuple("PostCommand", ["username", "message"])
ReadCommand = namedtuple("ReadCommand", ["username"])
FollowCommand = namedtuple("FollowCommand", ["username", "target"])
WallCommand = namedtuple("WallCommand", ["username"])


def parse(user_input):
    user_input = user_input.strip()

    if " -> " in user_input:
        parts = user_input.split(" -> ", 1)
        return PostCommand(parts[0], parts[1])

    words = user_input.split()

    if len(words) == 3 and words[1] == "follows":
        return FollowCommand(words[0], words[2])

    if len(words) == 2 and words[1] == "wall":
        return WallCommand(words[0])

    if len(words) == 1:
        return ReadCommand(words[0])

    return None

from social.clock import Clock
from social.post import Post


class SocialNetwork:
    def __init__(self, clock=None):
        self.clock = clock or Clock()
        self._posts = {}
        self._following = {}

    def post(self, username, message):
        if username not in self._posts:
            self._posts[username] = []
        self._posts[username].append(
            Post(username, message, self.clock.now())
        )

    def read(self, username):
        posts = self._posts.get(username, [])
        return sorted(posts, key=lambda p: p.timestamp, reverse=True)

    def follow(self, username, target):
        if username not in self._following:
            self._following[username] = set()
        self._following[username].add(target)

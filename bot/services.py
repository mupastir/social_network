import random

from strategies import (LikePostRequestStrategy,
                         UserPostRequestStrategy,
                         PostPostRequestStrategy)
from factories import RandomUserFactory, RandomPostFactory
from parsers import IniParser


class RandomRequestsService:

    CONFIG_PARSER = IniParser

    def __init__(self, config_path=None):
        config = self.CONFIG_PARSER(config_path).parse()
        self.number_of_users = config['BOT_LIMITS']['number_of_users']
        self.max_posts_per_user = config['BOT_LIMITS']['max_posts_per_user']
        self.max_likes_per_user = config['BOT_LIMITS']['max_likes_per_user']
        self.users = []
        self.posts = []

    def create_entities(self):
        self._create_users()
        self._create_posts()

    def post_entities(self):
        self._post_users()
        self._post_posts()
        self._post_likes()

    def _create_users(self):
        for _ in range(self.number_of_users):
            u = RandomUserFactory().create()
            self.users.append(u)

    def _create_posts(self):
        for _ in range(self.max_posts_per_user):
            post = RandomPostFactory().create()
            self.posts.append(post)

    def _post_likes(self):
        for user in (
                user for user
                in self.users
                if user.likes_count < self.max_likes_per_user):
            LikePostRequestStrategy.post(random.choice(self.posts), user)

    def _post_posts(self):
        for post in self.posts:
            PostPostRequestStrategy.post(post, random.choice(
                [user for user
                 in self.users
                 if user.posts_count < self.max_posts_per_user]
            ))

    def _post_users(self):
        for user in self.users:
            UserPostRequestStrategy.post(user)

    def execute(self):
        self.create_entities()
        self.post_entities()

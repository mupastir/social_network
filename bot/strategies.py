from abc import ABC, abstractmethod

from constants import *
import requests


class PostRequestStrategy(ABC):

    @abstractmethod
    def post(self, *args, **kwargs):
        pass


class UserPostRequestStrategy(PostRequestStrategy):

    @classmethod
    def post(cls, user):
        res = requests.post(url=REGISTER_URL, data=user.to_dict())
        user.jwt = res.json().get('token')


class PostPostRequestStrategy(PostRequestStrategy):

    @classmethod
    def post(cls, post, user):
        headers = {'Authorization': f'JWT {user.get_jwt()}'}
        res = requests.post(url=POSTS_CREATE_URL,
                            data=post.to_dict(),
                            headers=headers)
        post.id = res.json().get('id')
        user.increment_posts_count()


class LikePostRequestStrategy(PostRequestStrategy):

    @classmethod
    def post(cls, post, user):
        headers = {'Authorization': f'JWT {user.get_jwt()}'}
        requests.post(url=POSTS_LIKE_TEMPLATE_URL.format(post.id),
                      data={},
                      headers=headers)
        user.increment_likes_count()

from abc import ABC, abstractmethod


class PostableEntity(ABC):

    @abstractmethod
    def to_dict(self):
        pass


class User(PostableEntity):

    def __init__(self, *,
                 username=None,
                 email=None,
                 password=None,
                 first_name=None,
                 last_name=None,
                 phone=None,
                 ):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.posts_count = 0
        self.likes_count = 0
        self.jwt = None

    def increment_posts_count(self):
        self.posts_count += 1

    def increment_likes_count(self):
        self.likes_count += 1

    def get_jwt(self):
        if self.jwt:
            return self.jwt
        raise AttributeError("User doesn't have JWT. Log in or register")

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password1": self.password,
            "password2": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
        }

    def __str__(self):
        return repr(self.to_dict())


class Post(PostableEntity):

    def __init__(self, *, title, content, user: User = None):
        self.user = user
        self.content = content
        self.title = title
        self.id = None

    def to_dict(self):
        return {
            "content": self.content,
            "title": self.title,
        }

    def get_id(self):
        if self.id:
            return self.id
        raise AttributeError("Post doesn't have ID")

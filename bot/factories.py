from abc import abstractmethod, ABC

from faker import Faker
from faker.utils.text import slugify
from faker.providers import internet

from entities import User, Post

fake = Faker()
fake.add_provider(internet)


class EntityFactory(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create(self):
        raise NotImplementedError


class RandomUserFactory(EntityFactory):

    fake = fake

    def create(self) -> User:
        return User(
            username=slugify(self.fake.name()),
            email=self.fake.email(),
            password=self.fake.password(),
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            phone=self.fake.last_name()
        )


class RandomPostFactory(EntityFactory):

    fake = fake

    def create(self) -> Post:
        return Post(
            title=self.fake.name(),
            content=self.fake.text(),
        )

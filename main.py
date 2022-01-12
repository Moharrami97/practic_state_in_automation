# I want to send a letter in a hierarchical manner from the client to the manager.
# this is an exercise to learn the state design pattern.
from abc import ABC, abstractmethod


class Message:
    def __init__(self, subject, body, sender):
        self.subject = subject
        self.body = body
        self.sender = sender
        self.flow = [sender]

    def send(self, to_use):
        pass


class AbstractUSer(ABC):
    @property
    @abstractmethod
    def allowed(self):
        pass


class ManagingDirector(AbstractUSer):
    allowed = []


class InternalManger(AbstractUSer):
    allowed = [ManagingDirector]


class Supervisor(AbstractUSer):
    allowed = [InternalManger]


class Operator(AbstractUSer):
    allowed = [Supervisor]


class Client(AbstractUSer):
    allowed = [Operator]


if __name__ == "__main__":
    opt = Operator()
    spr = Supervisor()
    inm = InternalManger()
    mnd = ManagingDirector()
    client = Client()

    message = Message("Issue #123", "Issue description", client)

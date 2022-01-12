# I want to send a letter in a hierarchical manner from the client to the manager.
# this is an exercise to learn the state design pattern.
from abc import ABC, abstractmethod


class Message:
    def __init__(self, subject, body, sender):
        self.subject = subject
        self.body = body
        self.sender = sender
        self.flow = [sender]

    @property
    def current(self):
        return self.flow[-1]

    def send(self, to_use):
        if to_use.__class__ not in self.current.allowed:
            print(f"{self.current.__class__} is not allowed to send email to {to_use.__class__}")
        else:
            self.flow.append(to_use)
            print(f"message send to {to_use.__class__}")


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

    message.send(opt)
    message.send(spr)
    message.send(inm)
    message.send(mnd)

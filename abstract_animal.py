from abc import ABCMeta, abstractmethod


class AbstractAnimal(metaclass=ABCMeta):
    def __init__(self, name=None, energy=None, **kwargs):
        self.name = name
        self.energy = energy

    def say(self) -> None:
        print(f"Hello, I'm {self.__class__.__name__} and my name is {self.name}")

    def get_energy(self) -> int:
        return self.energy

    @abstractmethod
    def run(self) -> None:
        ...

    @abstractmethod
    def swim(self) -> None:
        ...

    @abstractmethod
    def fly(self) -> None:
        ...

from abstract_animal import AbstractAnimal


class Fish(AbstractAnimal):
    def __init__(self, name, energy=100, **kwargs):
        super(Fish, self).__init__(name, energy, **kwargs)

    def run(self) -> None:
        print(f"My name is {self.name} and I can't run")

    def swim(self) -> None:
        print(f"My name is {self.name} and I'm swimming")
        self.energy = self.energy - 5

    def fly(self) -> None:
        print(f"My name is {self.name} and I can't fly")


class FlyingFish(Fish):
    def fly(self) -> None:
        print(f"My name is " + str(self.name) + " and I'm flying")
        self.energy = self.energy - 20

from abstract_animal import AbstractAnimal


class Cat(AbstractAnimal):
    def __init__(self, name, energy=100, **kwargs):
        super(Cat, self).__init__(name, energy, **kwargs)

    def run(self) -> None:
        print("My name is " + str(self.name) + " and I'm running")
        self.energy = self.energy - 5

    def swim(self) -> None:
        print("My name is " + str(self.name) + " and I can't swim")

    def fly(self) -> None:
        print('My name is ' + str(self.name) + " and I can't fly")


class Tiger(Cat):
    def __init__(self, name, energy=200, **kwargs):
        super(Tiger, self).__init__(name, energy, **kwargs)

    def run(self) -> None:
        print("My name is " + str(self.name) + " and I'm running")
        self.energy = self.energy - 20

    def swim(self) -> None:
        print("My name is " + str(self.name) + " and I'm swimming")
        self.energy = self.energy - 40

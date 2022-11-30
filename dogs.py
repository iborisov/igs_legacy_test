from abstract_animal import AbstractAnimal


class Dog(AbstractAnimal):
    def __init__(self, name, energy=100, **kwargs):
        super().__init__(name, energy, **kwargs)

    def run(self):
        print(f"My name is {self.name} and I'm running")
        self.energy = self.energy - 10

    def swim(self):
        print(f"My name is {self.name} and I'm swimming")
        self.energy = self.energy - 30

    def fly(self):
        print(f"My name is {self.name} and I can't fly")

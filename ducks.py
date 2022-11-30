from abstract_animal import AbstractAnimal


class Duck(AbstractAnimal):
    def __init__(self, name, energy=100, **kwargs):
        super().__init__(name, energy, **kwargs)

    def run(self):
        print(f"My name is {self.name} and I can't run")

    def swim(self):
        print(f"My name is {self.name} and I'm swimming")
        self.energy = self.energy - 10

    def fly(self):
        print(f"My name is {self.name} and I'm flying")
        self.energy = self.energy - 30

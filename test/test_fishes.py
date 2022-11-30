import unittest

from fishes import Fish, FlyingFish
from test.utils import capture_stdout


class TestFish(unittest.TestCase):

    def setUp(self):
        self.fish_name = "Dori"
        self.fish = Fish(self.fish_name)
        self.DEFAULT_ENERGY = self.fish.get_energy()

    def test_say_should_greet(self):
        stdout = capture_stdout(self.fish.say)
        self.assertEqual(f"Hello, I'm Fish and my name is {self.fish_name}\n", stdout)

    def test_initial_energy_should_be_equal_to_default(self):
        self.assertEqual(self.DEFAULT_ENERGY, self.fish.get_energy())

    def test_run_should_not_change_energy(self):
        stdout = capture_stdout(self.fish.run)
        self.assertEqual(f"My name is {self.fish_name} and I can't run\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY, self.fish.get_energy())

    def test_swim_should_decrease_energy(self):
        stdout = capture_stdout(self.fish.swim)
        self.assertEqual(f"My name is {self.fish_name} and I'm swimming\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY - 5, self.fish.get_energy())

    def test_fly_should_not_change_energy(self):
        stdout = capture_stdout(self.fish.fly)
        self.assertEqual(f"My name is {self.fish_name} and I can't fly\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY, self.fish.get_energy())


class TestFlyingFish(unittest.TestCase):

    def setUp(self):
        self.fish_name = "Dori"
        self.fish = FlyingFish(self.fish_name)
        self.DEFAULT_ENERGY = self.fish.get_energy()

    def test_say_should_greet(self):
        stdout = capture_stdout(self.fish.say)
        self.assertEqual(f"Hello, I'm FlyingFish and my name is {self.fish_name}\n", stdout)

    def test_initial_energy_should_be_equal_to_default(self):
        self.assertEqual(self.DEFAULT_ENERGY, self.fish.get_energy())

    def test_run_should_not_change_energy(self):
        stdout = capture_stdout(self.fish.run)
        self.assertEqual(f"My name is {self.fish_name} and I can't run\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY, self.fish.get_energy())

    def test_swim_should_decrease_energy(self):
        stdout = capture_stdout(self.fish.swim)
        self.assertEqual(f"My name is {self.fish_name} and I'm swimming\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY - 5, self.fish.get_energy())

    def test_fly_should_decrease_energy(self):
        stdout = capture_stdout(self.fish.fly)
        self.assertEqual(f"My name is {self.fish_name} and I'm flying\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY - 20, self.fish.get_energy())


if __name__ == '__main__':
    unittest.main()

import unittest

from ducks import Duck
from test.utils import capture_stdout


class TestDuck(unittest.TestCase):

    def setUp(self):
        self.duck_name = "Donald"
        self.duck = Duck(self.duck_name)
        self.DEFAULT_ENERGY = self.duck.get_energy()

    def test_say_should_greet(self):
        stdout = capture_stdout(self.duck.say)
        self.assertEqual(f"Hello, I'm Duck and my name is {self.duck_name}\n", stdout)

    def test_initial_energy_should_be_equal_to_default(self):
        self.assertEqual(self.DEFAULT_ENERGY, self.duck.get_energy())

    def test_run_should_not_change_energy(self):
        stdout = capture_stdout(self.duck.run)
        self.assertEqual(f"My name is {self.duck_name} and I can't run\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY, self.duck.get_energy())

    def test_swim_should_decrease_energy(self):
        stdout = capture_stdout(self.duck.swim)
        self.assertEqual(f"My name is {self.duck_name} and I'm swimming\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY - 10, self.duck.get_energy())

    def test_fly_should_decrease_energy(self):
        stdout = capture_stdout(self.duck.fly)
        self.assertEqual(f"My name is {self.duck_name} and I'm flying\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY - 30, self.duck.get_energy())


if __name__ == '__main__':
    unittest.main()

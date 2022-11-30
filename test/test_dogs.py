import unittest

from dogs import Dog
from test.utils import capture_stdout


class TestDog(unittest.TestCase):

    def setUp(self):
        self.dog_name = "Bobik"
        self.dog = Dog(self.dog_name)
        self.DEFAULT_ENERGY = self.dog.get_energy()

    def test_say_should_greet(self):
        stdout = capture_stdout(self.dog.say)
        self.assertEqual(f"Hello, I'm Dog and my name is {self.dog_name}\n", stdout)

    def test_initial_energy_should_be_equal_to_default(self):
        self.assertEqual(self.DEFAULT_ENERGY, self.dog.get_energy())

    def test_run_should_decrease_energy(self):
        stdout = capture_stdout(self.dog.run)
        self.assertEqual(f"My name is {self.dog_name} and I'm running\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY - 10, self.dog.get_energy())

    def test_swim_should_decrease_energy(self):
        stdout = capture_stdout(self.dog.swim)
        self.assertEqual(f"My name is {self.dog_name} and I'm swimming\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY - 30, self.dog.get_energy())

    def test_fly_should_not_change_energy(self):
        stdout = capture_stdout(self.dog.fly)
        self.assertEqual(f"My name is {self.dog_name} and I can't fly\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY, self.dog.get_energy())


if __name__ == '__main__':
    unittest.main()

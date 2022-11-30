import unittest

from cats import Cat, Tiger
from test.utils import capture_stdout


class TestCat(unittest.TestCase):

    def setUp(self):
        self.cat_name = "Barsik"
        self.cat = Cat(self.cat_name)
        self.DEFAULT_ENERGY = self.cat.get_energy()

    def test_say_should_greet(self):
        stdout = capture_stdout(self.cat.say)
        self.assertEqual(f"Hello, I'm Cat and my name is {self.cat_name}\n", stdout)

    def test_initial_energy_should_be_equal_to_default(self):
        self.assertEqual(self.DEFAULT_ENERGY, self.cat.get_energy())

    def test_run_should_decrease_energy(self):
        stdout = capture_stdout(self.cat.run)
        self.assertEqual(f"My name is {self.cat_name} and I'm running\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY - 5, self.cat.get_energy())

    def test_swim_should_not_change_energy(self):
        stdout = capture_stdout(self.cat.swim)
        self.assertEqual(f"My name is {self.cat_name} and I can't swim\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY, self.cat.get_energy())

    def test_fly_should_not_change_energy(self):
        stdout = capture_stdout(self.cat.fly)
        self.assertEqual(f"My name is {self.cat_name} and I can't fly\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY, self.cat.get_energy())


class TestTiger(unittest.TestCase):

    def setUp(self):
        self.tiger_name = "Simba"
        self.tiger = Tiger(self.tiger_name)
        self.DEFAULT_ENERGY = self.tiger.get_energy()

    def test_say_should_greet(self):
        stdout = capture_stdout(self.tiger.say)
        self.assertEqual(f"Hello, I'm Tiger and my name is {self.tiger_name}\n", stdout)

    def test_initial_energy_should_be_equal_to_default(self):
        self.assertEqual(self.DEFAULT_ENERGY, self.tiger.get_energy())

    def test_run_should_decrease_energy(self):
        stdout = capture_stdout(self.tiger.run)
        self.assertEqual(f"My name is {self.tiger_name} and I'm running\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY - 20, self.tiger.get_energy())

    def test_swim_should_decrease_energy(self):
        stdout = capture_stdout(self.tiger.swim)
        self.assertEqual(f"My name is {self.tiger_name} and I'm swimming\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY - 40, self.tiger.get_energy())

    def test_fly_should_not_change_energy(self):
        stdout = capture_stdout(self.tiger.fly)
        self.assertEqual(f"My name is {self.tiger_name} and I can't fly\n", stdout)
        self.assertEqual(self.DEFAULT_ENERGY, self.tiger.get_energy())


if __name__ == '__main__':
    unittest.main()

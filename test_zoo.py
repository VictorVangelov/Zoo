import unittest
from zoo import Zoo


class TestZoo(unittest.TestCase):

    def setUp(self):
        self.new_zoo = Zoo(20, 5000)

    def test_init(self):
        self.assertEqual(20, self.new_zoo.capacity)
        self.assertEqual(5000, self.new_zoo.budget)
        self.assertEqual(0, len(self.new_zoo.dict_of_animals))

    def test_accommodate(self):
        self.assertEqual({"Lion": 1}, self.new_zoo.accomodate("Lion"))
        self.assertEqual({"Lion": 2}, self.new_zoo.accomodate("Lion"))

    def test_dayly_income(self):
        self.new_zoo.accomodate("Lion")
        self.new_zoo.accomodate("Lion")
        self.new_zoo.accomodate("Koala")
        self.assertEqual(180, self.new_zoo.daily_income())

if __name__ == '__main__':
    unittest.main()

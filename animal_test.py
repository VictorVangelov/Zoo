from animal import Animal

import unittest


class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.test_animal = Animal("coala", 7, "Willie", "male", 92)

    def test_animal_init(self):
        self.assertEqual("coala", self.test_animal.species)
        self.assertEqual(self.test_animal.age, 7)
        self.assertEqual(self.test_animal.name, "Willie")
        self.assertEqual(self.test_animal.gender, "male")
        self.assertEqual(self.test_animal.weight, 92)

    def test_grow(self):
        pass


if __name__ == '__main__':
    unittest.main()

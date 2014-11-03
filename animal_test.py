from animal import Animal

import unittest


class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.test_animal = Animal("coala", 7, "Willie", "male", 92, "herbivore")

    def test_animal_init(self):
        self.assertEqual("coala", self.test_animal.species)
        self.assertEqual(self.test_animal.age, 7)
        self.assertEqual(self.test_animal.name, "Willie")
        self.assertEqual(self.test_animal.gender, "male")
        self.assertEqual(self.test_animal.weight, 92)
        self.assertEqual(self.test_animal.food_type, "herbivore")

    def test_grow(self):
        self.assertGreater(self.test_animal.weight)
        self.assertGreater(self.test_animal.age)

    def test_average_weight(self):
        self.assertEqual(self.test_animal.average_weight, 15)

    def test_animal_eats(self):
        pass

    def test_animal_dead(self):
        pass

    def test_animal_is_alive(self):
        pass




if __name__ == '__main__':
    unittest.main()

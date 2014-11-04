import json


class Zoo():

    dict_of_species_information = {
        "Elephant": {"average_weight": 5000, "life_expectancy": 50 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 1, "newborn_average_weight": 100, "weight/age": 50, "food/weight": 0.1},
        "Horse": {"average_weight": 521, "life_expectancy": 15 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 3, "newborn_average_weight": 15, "weight/age": 23, "food/weight": 0.1},
        "Cow": {"average_weight": 465, "life_expectancy": 10 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 2, "newborn_average_weight": 10, "weight/age": 20, "food/weight": 0.1},
        "Wolf": {"average_weight": 36, "life_expectancy": 12 * 365, "food_type": "carnivore", "gestation_period": "24", "num_of_newborns": 2, "newborn_average_weight": 2, "weight/age": 2, "food/weight": 0.1},
        "Gorilla": {"average_weight": 207, "life_expectancy": 22 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 1, "newborn_average_weight": 9, "weight/age": 11, "food/weight": 0.04},
        "Kangaroo": {"average_weight": 35, "life_expectancy": 25 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 3, "newborn_average_weight": 1.5, "weight/age": 2, "food/weight": 0.3},
        "Koala": {"average_weight": 15, "life_expectancy": 30 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 2, "newborn_average_weight": 1, "weight/age": 1, "food/weight": 0.4},
        "Sheep": {"average_weight": 55.5, "life_expectancy": 12 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 3, "newborn_average_weight": 4, "weight/age": 5, "food/weight": 0.1},
        "Jaguar": {"average_weight": 100, "life_expectancy": 33 * 365, "food_type": "carnivore", "gestation_period": "24", "num_of_newborns": 1, "newborn_average_weight": 9, "weight/age": 7, "food/weight": 0.2},
        "Pig": {"average_weight": 192, "life_expectancy": 12 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 2, "newborn_average_weight": 10, "weight/age": 10, "food/weight": 0.1}, }

    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.dict_of_animals = {}

    def save(self, filename):
        dict_for_species = {}
        for breed in Zoo.dict_of_species_information:
            dict_for_species[breed] = Zoo.dict_of_species_information[breed]
        file = open(filename, "w")
        file.write(json.dumps(dict_for_species))
        file.close()
# dict = {'tiger': ['toshko', 'boshko']}
# tigers = dict['tiger']
# tigers.remove('toshko')
    def accomodate(self, new_animal):
        if new_animal in self.dict_of_animals.keys():
            self.dict_of_animals[new_animal] += 1
        else:
            self.dict_of_animals[new_animal] = 1
        return self.dict_of_animals

    def daily_income(self):
        return sum(self.dict_of_animals.values()) * 60

    def daily_outcome(self):
        pass

    def load(self, filename):
        file = open(filename, "r")
        content = json.load(file)
        for breed in content:
            Zoo.dict_of_species_information[breed] = content[breed]



if __name__ == '__main__':
    for specie in Zoo.dict_of_species_information:
        print(specie)

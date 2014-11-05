from animal import Animal
import json


class Zoo():

    DAILY_INCOME_PER_ANIMAL = 60
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

    def daily_outcome(self):
        total_outcome = 0
        for animal in self.dict_of_animals.keys():
            info = self.dict_of_species_information[animal]
            if info[food_type] == "carnivore":
                total_outcome += self.dict_of_animals[animal] * 4
            elif info[food_type] == "herbivore":
                total_outcome += self.dict_of_animals[animal] * 2
        return total_outcome
        self.budget -= total_outcome

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

    def accommodate(self, new_animal):

        if new_animal.species in self.dict_of_animals:
            self.dict_of_animals[new_animal.species].add(new_animal)
        else:
            self.dict_of_animals[new_animal.specie] = []
            self.dict_of_animals.add(new_animal)
            self.set_new_breed_information()

    def set_new_breed_information():
        pass


    def daily_income(self):
        numm_of_all_animals = 0
        for breed in self.dict_of_animals:
            numm_of_all_animals += len(self.dict_of_animals[breed])
        income = numm_of_all_animals * Zoo.DAILY_INCOME_PER_ANIMAL
        self.budget += income
        return income


    def check_if_dead(self):
        for animal in self.dict_of_animals.keys():
            if Animal.get_chance_of_diyng(animal) == 1:
                self.dict_of_animals[animal] -= 1

    def load(self, filename):
        file = open(filename, "r")
        content = json.load(file)
        for breed in content:
            Zoo.dict_of_species_information[breed] = content[breed]

    def simulate(self, interval, period):
        days = self.convert_to_days(interval, period)
        if days is not False:
            for every_day in days:
                self.simulate_one_day()
        else:
            print("unknown interval type, please try again")
            self.input_command()

    def convert_to_days(self, interval, period):
        if interval == "week":
            return period*7
        elif interval == "mounth":
            return period*30
        elif interval == "day":
            return period
        else:
            return False

if __name__ == '__main__':
    for specie in Zoo.dict_of_species_information:
        print(specie)

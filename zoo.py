from animal import Animal
import json


class Zoo():

    DAILY_INCOME_PER_ANIMAL = 60
    PRICE_FOR_KILO_MEAT = 4
    PRICE_FOR_KILO_VEGETABLES = 2
    SIMULATION_PROFIT = 0

    dict_of_species_information = {
        "Elephant": {"average_weight": 5000, "life_expectancy": 50 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 1, "newborn_average_weight": 100, "weight_age": 50, "food_weight": 0.1},
        "Horse": {"average_weight": 521, "life_expectancy": 15 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 3, "newborn_average_weight": 15, "weight_age": 23, "food_weight": 0.1},
        "Cow": {"average_weight": 465, "life_expectancy": 10 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 2, "newborn_average_weight": 10, "weight_age": 20, "food_weight": 0.1},
        "Wolf": {"average_weight": 36, "life_expectancy": 12 * 365, "food_type": "carnivore", "gestation_period": "24", "num_of_newborns": 2, "newborn_average_weight": 2, "weight_age": 2, "food_weight": 0.1},
        "Gorilla": {"average_weight": 207, "life_expectancy": 22 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 1, "newborn_average_weight": 9, "weight_age": 11, "food_weight": 0.04},
        "Kangaroo": {"average_weight": 35, "life_expectancy": 25 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 3, "newborn_average_weight": 1.5, "weight_age": 2, "food_weight": 0.3},
        "Koala": {"average_weight": 15, "life_expectancy": 30 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 2, "newborn_average_weight": 1, "weight_age": 1, "food_weight": 0.4},
        "Sheep": {"average_weight": 55.5, "life_expectancy": 12 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 3, "newborn_average_weight": 4, "weight_age": 5, "food_weight": 0.1},
        "Jaguar": {"average_weight": 100, "life_expectancy": 33 * 365, "food_type": "carnivore", "gestation_period": "24", "num_of_newborns": 1, "newborn_average_weight": 9, "weight_age": 7, "food_weight": 0.2},
        "Pig": {"average_weight": 192, "life_expectancy": 12 * 365, "food_type": "herbivore", "gestation_period": "24", "num_of_newborns": 2, "newborn_average_weight": 10, "weight_age": 10, "food_weight": 0.1}, }

    AVERAGE_DAYS_IN_MOUNTH = 30
    DAYS_IN_WEEK = 7
    MOUNTHS_IN_YEAR = 12

    def set_new_breed_information():
        breed = input("Enter the name of the new breed")
        average_weight = input("Enter the average weight of the animal")
        life_expectancy = input("Enter the life expectancy of the animal(in mounth)")
        food_type = input("Enter the type of food that the breed eat")
        gestation_period = input("Enter how much mount")
        num_of_newborns = input("Enter the name of the new breed")
        newborn_average_weight = input("Enter the name of the new breed")
        weight_age = input("Enter the name of the new breed")
        food_weight = input("Enter the name of the new breed")
        Zoo.dict_of_species_information[breed] = {
            "average_weight": average_weight,
            "life_expectancy": life_expectancy,
            "food_type": food_type,
            "gestation_period": gestation_period,
            "num_of_newborns": num_of_newborns,
            "newborn_average_weight": newborn_average_weight,
            "weight/age": weight_age,
            "food/weight": food_weight
        },

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

    def accommodate(self, new_animal):

        if new_animal.species in self.dict_of_animals:
            self.dict_of_animals[new_animal.species].add(new_animal)
        else:
            self.dict_of_animals[new_animal.specie] = []
            self.dict_of_animals.add(new_animal)
            self.set_new_breed_information()

    def daily_income(self):
        num_of_all_animals = 0
        for breed in self.dict_of_animals:
            num_of_all_animals += len(self.dict_of_animals[breed])
        income = num_of_all_animals * Zoo.DAILY_INCOME_PER_ANIMAL
        self.budget += income
        return income

    def daily_outcome(self):
        total_outcome = 0
        for animal in self.dict_of_animals:
            info = self.dict_of_species_information[animal.species]
            if info.food_type == "carnivore":
                total_outcome += Zoo.PRICE_FOR_KILO_MEAT
            elif info.food_type == "herbivore":
                total_outcome += Zoo.PRICE_FOR_KILO_VEGETABLES
        self.budget -= total_outcome
        return total_outcome

    def check_if_dead(self):
        for animal in self.dict_of_animals:
            if Animal.get_chance_of_diyng(animal) == 1:
                self.dict_of_animals.remove(animal)

    def load(self, filename):
        file = open(filename, "r")
        content = json.load(file)
        for breed in content:
            Zoo.dict_of_species_information[breed] = content[breed]

    def simulate(self, interval, period):
        days = self.convert_interval_to_number(interval)
        if days is not False:
            for period in range(0, days):
                print(Zoo.SIMULATION_PROFIT)
                Zoo.SIMULATION_PROFIT = 0
                for day in range (0, days):
                    self.simulate_one_day()
        else:
            print("unknown interval type, please try again")
            self.input_command()

    def convert_interval_to_number(self, interval):
        if interval == "week":
            return Zoo.DAYS_IN_WEEK
        elif interval == "mounth":
            return Zoo.AVERAGE_DAYS_IN_MOUNTH
        elif interval == "day":
            return 1
        elif interval == "year":
            return Zoo.AVERAGE_DAYS_IN_MOUNTH * Zoo.MOUNTHS_IN_YEAR
        else:
            return False

    def move_to_habitat(self, breed, name):
        for animal in self.dict_of_animals[breed]:
            if name == animal.name:
                self.dict_of_animals[breed].remove(animal)

    def simulate_one_day(self):
        self.feed_all_animals()
        Zoo.SIMULATION_PROFIT -= self.daily_outcome
        Zoo.SIMULATION_PROFIT += self.daily_income

    def feed_all_animals(self):
        for breed in self.dict_of_animals:
            for animal in self.dict_of_animals[breed]:
                animal.eat()


if __name__ == '__main__':
    for specie in Zoo.dict_of_species_information:
        print(specie)

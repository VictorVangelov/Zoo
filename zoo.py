from animal import Animal
import json


class Zoo():

    DAILY_INCOME_PER_ANIMAL = 60
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
            return period*Zoo.DAYS_IN_WEEK
        elif interval == "mounth":
            return period*Zoo.AVERAGE_DAYS_IN_MOUNTH
        elif interval == "day":
            return period
        elif interval == "year":
            return period * Zoo.AVERAGE_DAYS_IN_MOUNTH * Zoo.MOUNTHS_IN_YEAR
        else:
            return False

    def move_to_habitat(self, breed, name):
        for animal in self.dict_of_animals[breed]:
            if name == animal.name:
                self.dict_of_animals[breed].remove(animal)

    def feed_all_animals(self):
        /


if __name__ == '__main__':
    for specie in Zoo.dict_of_species_information:
        print(specie)

class Animal:

    def __init__(self, species, age, name, gender, weight, food_type):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.average_weight = 50
        self.food_type = food_type
        self.dict_of_species_information = {"Elephant" : {"average_weight": 5000, "life_expectancy": 50*365},
         "Horse":{"average_weight": 521, "life_expectancy": 15*365} , "Cow": {"average_weight": 465, "life_expectancy": 10*365},
          "Wolf" :{"average_weight": 36, "life_expectancy": 12*365}, "Gorilla":{"average_weight": 207, "life_expectancy": 22*365} ,
           "Kangaroo": {"average_weight": 35, "life_expectancy": 25*365},           "Koala":{"average_weight": 15, "life_expectancy": 30*365} ,
            "Sheep": {"average_weight": 55.5, "life_expectancy": 12*365}, "Jaguar": {"average_weight": 100, "life_expectancy": 33*365},
            "Pig": {"average_weight": 192, "life_expectancy": 12*365} }

    def grow(self, amount_food):
        if self.weight < self.average_weight:
            if self.food_type == "meat":
                self.weight += amount_food * 0.2
            else:
                self.weight += amount_food * 0.1
        self.age += 1

    def set_average_weight(self, specie):
        if specie in self.dict_of_average_weight:
            self.average_weight = self.dict_of_average_weight[specie]
        else:
            new_average_weight = raw_input("Enter new average weight for this specie >")
            self.average_weight = new_average_weight

    def eat(self, amount_food):
        print("im eating and growing")
        self.grow(amount_food)

    def get_chance_of_dying(self):
        return (self.age / self.life_expectancy)

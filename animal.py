class Animal:


    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight

    def grow(self, amount_food):
        if self.weight < self.average_weight:
            self.age
        self.age += 1

    def set_average_weight(self, specie):
        if specie in self.dict_of_average_weight:
            self.average_weight = self.dict_of_average_weight[specie]
        else:
            new_average_weight = raw_input(
                "Enter new average weight for this specie >")
            self.average_weight = new_average_weight

    def eat(self, amount_food):
        print("im eating and growing")
        self.grow(amount_food)

    def get_chance_of_dying(self):
        return (self.age / self.life_expectancy)

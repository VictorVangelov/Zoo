class Zoo():

    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.dict_of_animals = {}

    def accomodate(self, new_animal):
        return self.dict_of_animals.append(new_animal)



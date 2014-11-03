class Zoo():

    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.dict_of_animals = {}

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

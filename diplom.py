class Human:

    def __init__(self, first_name, last_name, fathers_name, gender, date_birth, date_death):
        self.first_name = first_name
        self.last_name = last_name
        self.fathers_name = fathers_name
        self.gender = gender
        self.date_birth = date_birth
        self.date_death = date_death

    def __str__(self):
        return (f'{self.first_name} {self.last_name} {self.fathers_name}\n'
                f'Gender: {self.gender}\n{self.date_birth} - {self.date_death}\n'
                f'---')


class Database:

    def __init__(self):
        self.database = set()

    def find_human(self, first_name):
        for human in self.database:
            if human.first_name == first_name:
                return human
        return None

    def add_human(self, human):
        self.database.add(human)

    def delete_human(self, first_name):
        human = self.find_human(first_name)
        if human:
            self.database.remove(human)

...
while True:
    first_name_ = input('(necessary)Input name: ')
    if first_name_:
        break

last_name_ = input('(not necessary)Input last name: ')
if not last_name_:
    last_name_ = None

fathers_name_ = input('(not necessary)Input father`s name: ')
if not fathers_name_:
    fathers_name_ = None

while True:
    gender_ = input('(necessary)Input gender: ')
    if gender_:
        break

while True:
    date_birth_ = input('(necessary)Input date of birth: ')
    if date_birth_:
        break

date_death_ = input('(not necessary)Input date of death: ')
if not date_death_:
    date_death_ = None
...
h1 = Human(first_name_, last_name_, fathers_name_, gender_, date_birth_, date_death_)
print(h1.__str__())
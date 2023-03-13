class Animal:
    def __init__(self, sex, age):
        self.sex = sex
        self.age = age


class Human(Animal):
    def __init__(self, sex, age, name, nation, job):
        super().__init__(sex, age)
        self.name = name
        self.nation = nation
        self.job = job
    
    def info(self):
        print(f"sex:{self.sex} age:{self.age} name:{self.name} nation:{self.nation} job:{self.job}")


class Dogs(Animal):
    def __init__(self, sex, age, species):
        super().__init__(sex, age)
        self.species = species
        
    def info(self):
        print(f"sex:{self.sex} age:{self.age} species:{self.species}")


shota = Human('male', 23, 'Shota', 'japan', 'engineer')
shota.info()

ginjiro = Human('male', 24, 'Ginjiro', 'japan', 'engineer')
ginjiro.info()

chihuahua = Dogs('male', 2, 'chihuahua')
chihuahua.info()

dachshund = Dogs('female', 1, 'dachshund')
dachshund.info()
class Animal(object):
    def __init__(self, sex_animals, age_animals):
        self._sex_animals = sex_animals
        self._age_animals = age_animals
        
    @property
    def sex_animals(self):
        return self._sex_animals
    
    @sex_animals.setter
    def sex_animals(self, Sex):
        self.sex = Sex
    
    @property
    def age_animals(self):
        return self._age_animals
    
    @age_animals.setter
    def age_animals(self, Age):
        self.age_animals = Age
    
        
class Human(Animal):
    def __init__(self, sex, age, name, nation, job):
        self.sex = sex
        self.age = age
        self._name = name
        self._nation = nation
        self._job = job
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, Name):
        self.name = Name
    
    @property
    def nation(self):
        return self._nation
    
    @nation.setter
    def nation(self, Nation):
        self.nation = Nation
    
    @property
    def job(self):
        return self._job
        
    @job.setter
    def job(self, Job):
        self.job = Job
        
    def info(self):
        print(f"sex:{self.sex} age:{self.age} name:{self.name} nation:{self.nation} job:{self.job}")
    
    
class Dogs(Animal):
    def __init__(self, sex_dogs, age_dogs, species_dogs):
        self.sex_dogs = sex_dogs
        self.age_dogs = age_dogs
        self._species_dogs = species_dogs
        
    @property
    def species_dogs(self):
        return self._species_dogs
    
    @species_dogs.setter
    def species_dogs(self, Species):
        self.species_dogs = Species
        
    def info(self):
        print(f"sex:{self.sex_dogs} age:{self.age_dogs} species:{self.species_dogs}")
    
    
shota = Human('male', 23, 'Shota', 'japan', 'engineer')
shota.info()
ginjiro = Human('male', 24, 'Ginjiro', 'japan', 'engineer')
ginjiro.info()

chihuahua = Dogs('male', 2, 'chihuahua')
chihuahua.info()
dachshund = Dogs('female', 1, 'dachshund')
dachshund.info()
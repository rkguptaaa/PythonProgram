####### One way

#class Cat:
#    species = 'mammal'
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#    
#    def FindEldestCat(self):
#        return self.age
#
#cat_instance = []
#cat_age = []
#
#cat_instance.append(Cat('cat1', 59))
#cat_instance.append(Cat('cat2', 25))
#cat_instance.append(Cat('cat3', 55))
#
#for instance in cat_instance:
#    cat_age.append(instance.FindEldestCat())
#
#print(f'the max age among the cat is {max(cat_age)}')

####### Second way

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat_instance = []

cat_instance.append(Cat('cat1', 59))
cat_instance.append(Cat('cat2', 25))
cat_instance.append(Cat('cat3', 55))

    
def FindEldestCat(instances):
    age = []
    for instance in instances:
       age.append(instance.age)
    return max(age)

@classmethod
def adding_things(cls, num1, num2):
    return cls('ravi', num1 + num2)

@staticmethod
def adding_things2(num1, num2):
    return num1 + num2

print(f'the max age among the cat is {FindEldestCat(cat_instance)}')
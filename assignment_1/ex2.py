for i in range(10):
    print(i)

for i in range(3, 10):
    print(i)

for i in range(0, 10, 2):
    print(i)

i = 0
while i < 10:
    i += 1
    print(i)

def sign(x):
    if x > 0:
        return 'postive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))

class Student(object):
    def __init__(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_major(self, major):
        self.major = major

anna = Student('anna')
anna.set_age(21)
anna.set_major('physics')

class MasterStudent(Student):
    def set_lab(self, lab):
        self.lab = lab

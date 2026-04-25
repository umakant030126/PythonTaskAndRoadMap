# static method  -  defined inside a class which is neither bound to the object nor to the class.
# To create a static method , use staticmethod decorator.

class Student:
    '''
    Student class store info about students and their activities.
    '''
    departments = ["Fin","Admin","Tech","CSE","ME"]
    college_name = "ABC Institute"

    def __init__(self, name , roll_number ):
        print("Objected created and initialize...!")
        self.name = name
        self.roll_number =roll_number


    def studiesHours(self, n_hrs):
        print(self)
        print(f"Student studies {n_hrs} per day in {self.college_name}")

    def fevSports(self, sports_name):
        print(self)
        print(f"Student like play {sports_name} in {self.college_name}")

    @staticmethod
    def greet():
        print(f"Welcome to college..!")

    @classmethod
    def getDept(cls):
        print(f"Department in {cls.college_name} are :")
        for dept in cls.departments:
            print(dept)

s1 = Student("John", 10001)
s1.studiesHours(5)
print("---------------------")
s1.greet()
s1.getDept()

print("**************************")
help(Student)
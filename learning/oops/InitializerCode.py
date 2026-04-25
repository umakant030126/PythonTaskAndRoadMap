# __init__() method
# is an instance method
# it is used to create and initialize the attributes during the object.

class Student:
    def __init__(self, name , roll_number , dept):
        print("Objected created and initialize...!")
        self.name = name
        self.roll_number =roll_number
        self.dept = dept


s1 = Student("John",1001,"FIN")
s1.branch = "DEL"

print(s1.__dict__)
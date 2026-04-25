class Student:
    """
    This is class Student to manage student info and activities.
    """
    pass


# doc strings => __doc__

s1 = Student()
s2 = Student()

print(Student.__doc__)
print(help(Student))
print("************************************************")

s1.name = "John"
s1.age = 35
# use of __dict__ (Dunder dict) => it store variable name and its value as key value pair.
print(s1.__dict__)


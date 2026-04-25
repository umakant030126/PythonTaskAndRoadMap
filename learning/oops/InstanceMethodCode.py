class Student:
    def studiesHours(self, n_hrs):
        print(self)
        print(f"Student studies {n_hrs} per day")

    def fevSports(self, sports_name):
        print(self)
        print(f"Student like play {sports_name}")




s1 = Student()
s2 = Student()


s1.studiesHours(5)
s1.fevSports("Football")
print("**********************************")
s2.studiesHours(7)
s2.fevSports("Chess")

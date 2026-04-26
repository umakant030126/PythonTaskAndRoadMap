class Vehicle:
    company_name = "ABC moters"

    def __init__(self, n_wheels,n_seats, mileage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def getDetails(self):
        return f"This Vehicle have {self.n_wheels} and {self.n_seats} and provide mileage of {self.mileage} kmpl...!"


v1 = Vehicle(4,5,20)
print(v1.getDetails())
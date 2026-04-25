class PhoneBook:
    phone_directory = []

    def __init__(self, name , contact_number):
        self.name = name
        self.contact_number = contact_number
        PhoneBook.phone_directory.append(self)

    def showContact(self):
        return f"Name is {self.name} and contact number is {self.contact_number}"

    @classmethod
    def showPhoneDirectory(cls):
        if len(cls.phone_directory) == 0:
            print("No contact found , not added any number yet...!")
        else:
            for contact in cls.phone_directory:
                print(contact.showContact())


    @classmethod
    def searchContact(cls,search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.contact_number

        return f"No contact number found for {search_name}"

    @staticmethod
    def validate_contact_number(phone_number):
        if len(phone_number) >= 8 and phone_number.isdigit():
            return True
        else:
            return False


number_of_contact = int(input("How many contact you want to create ? :"))

for i in range(number_of_contact):
    contact_name = input("Enter name of contact : ")
    contact_phone_number = input("Enter contact number :")
    if PhoneBook.validate_contact_number(contact_phone_number):
        PhoneBook(contact_name,contact_phone_number)
    else:
        print(f"Invalid phone number for {contact_name}, phone number should be 8 or more char.")

# c1 = PhoneBook("John",123456789)
# c2 = PhoneBook("Carol",784596321)
# c3 = PhoneBook("Calum",458796231)
# print(c1.showContact())
# print(c2.showContact())
print("********************************")
# c1.showPhoneDirectory()
print("---------------------")
# print(PhoneBook.searchContact("John"))
# print(PhoneBook.searchContact("Alice"))
PhoneBook.showPhoneDirectory()
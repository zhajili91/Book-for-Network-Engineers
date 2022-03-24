# Python Object-Oriented Programming

class Employee:  # class is like an object constructor, or a "blueprint" for creating objects.

    number_of_employees = 0
    raise_amount = 1.2  # class attribute

    def __init__(self, first, last, pay,
                 was_born):  # The __init__() function/method is called automatically every time the
        # class is being used to create a new object.
        self.first = first  # attribute of class
        self.last = last  # attribute of class
        self.pay = pay  # attribute of class
        self.email = first.lower() + "." + last.lower() + "@ordubad.com"  # attribute of class
        self.was_born = was_born  # attribute of class
        Employee.number_of_employees = Employee.number_of_employees + 1

    def display_full_name(self):  # this is method/function ,by default self is always taken
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)


employee1 = Employee("Zeynal", "Hajili", 1000, "Ordubad")  # init method will run automatically to create employee1
# object ,employee1 will be passed as self to the function and arguments will be taken automatically
employee2 = Employee("Mamed", "Hajiyev", 2000, "Ordubad")
employee3 = Employee("Haji", "Hajiyev", 200, "Julfa")
employee4 = Employee("Huseyn", "Hajiyev", 999, "Baku")
employee5 = Employee("Bagi", "Mammadov", 0, "Baku")
print(Employee.number_of_employees)
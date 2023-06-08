#Parent Class User
class User:
    name = "Mark"
    email = "mark@gmail.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child Class Employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input ("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print ("Welcome back, {}!".format(entry_name))
        else:
            print ("The pin or email is incorrect")

#Child Class Customer
class Customer(User):
    code_number = "4321"


# This is the same method in the parent class "User"
# The difference is that, instead of using entry_password, we're using entry_pin.
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_code = input("Enter the code: ")
        if (entry_name == self.name and entry_code == self.code_number):
            print("Hello {}! Welcome!".format(entry_name))
        else:
            print("The code seems to be wrong...")

# The following code invokes the method inside each class for User and Employee.

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

customer2 = Customer()
customer2.getLoginInfo()

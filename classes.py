# OTP In Python 
# object oriented programming = شی گرایی

class AdminCode:
    code = 11
    key = 22
    password = 33

class AminCar:
    # main company = iran
    price = 32000
    color = ['black', 'red', 'green']
    maxspeed = 450
    

    def amin(self):
        newcolor = ['yellow', 'orange', 'blue']


FranceCar = AminCar()
print(FranceCar.color)



class Mohsencar(AminCar):
    pass 


AbassCar = Mohsencar()
print(Mohsencar.maxspeed)
# Python Inheritance
# ارث بری در کلاس های پایتون


class Student:
    def __init__(self, name, age, code):
        self.name = name
        self.age = age
        self.code = code





        
















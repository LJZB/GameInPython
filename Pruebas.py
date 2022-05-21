import os

os.system('cls')

#Programacióon Orientada a Objetos
class Employee():
    #Constructor
    def __init__(self, baseSalary, overtime, rate):
        self.baseSalary = baseSalary
        self.overtime = overtime
        self.rate = rate

    def getWage(self):
        return self.baseSalary + (self.overtime*self.rate)

#Herencia
class Engineer(Employee):
    def __init__(self, baseSalary, overtime, rate):
        self.baseSalary = baseSalary
        self.overtime = overtime
        self.rate = rate

class Doctor(Employee):
    def __init__(self, baseSalary, overtime, rate):
        print(f"I am a doctor and my salary is {baseSalary}")

Ross = Doctor(2000,23,70)

# Mark = Engineer(1000,15,10)
# print(Mark.getWage())

# Harry = Engineer(1500,12,15)
# print(Harry.getWage())


#employee1 = Employee(20000,13,20) #Creación de objeto de la clase Employee
#print('Employee 1 (POO) total salary is {}'.format(employee1.getWage()))

#employee2 = Employee(25000,12,19)
#print('Employee 2 (POO) total salary is {}'.format(employee2.getWage()))
import os

os.system('cls')

#Programacióon Orientada a Objetos

#Sin usar POO
baseSalary = 30000
overtime = 10
rate = 20

def getWage(baseSalary, overtime, rate):
    return baseSalary + (overtime*rate)

print('Employee 1 total salary is {}'.format(getWage(baseSalary, overtime, rate)))

#Usando POO
class Employee():
    baseSalary = 30000
    overtime = 10
    rate = 20

    def getWage(self):
        return self.baseSalary + (self.overtime*self.rate)

employe1 = Employee()
print('Employee 1 total salary is {}'.format(employe1.getWage()))
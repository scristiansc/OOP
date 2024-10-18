#Definicion de la clase

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary


    def increase_salary(self, percentage):
     self.salary += percentage / 100 * self.salary


    def decrease_salary(self, percentage):
       self.salary -= percentage / 100 * self.salary


    def show_information(self):
       print (f"Name: {self.name}")
       print (f"Age: {self.age}")
       print (f"Salary: {self.salary}")

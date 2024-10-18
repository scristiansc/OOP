from employee import Employee

employee_gabo = Employee("Gabriel", 25, 50_000)
employee_sindry = Employee("Sindry", 25, 30_000)

print (f"Base salary of {employee_gabo.name} is: {employee_gabo.salary}")
print (f"Base salary of {employee_sindry.name} is: {employee_sindry.salary}")

#Using def increase salary
employee_gabo.increase_salary(10)

#Using def decrease salary
employee_sindry.decrease_salary(10)

print (f"New salary of {employee_gabo.name} is: {employee_gabo.salary}")
print (f"New salary of {employee_sindry.name} is: {employee_sindry.salary}")

#Using def show information
print ("\nOur 1st employee is: ")
employee_gabo.show_information()

print ("\nOur 2nd employee is: ")
employee_sindry.show_information()
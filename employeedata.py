employees = [("Alice", 50000, "IT"), ("Bob", 45000, "HR"), ("Charlie", 60000, "IT")]

it_people = list(map(lambda emp: emp[0], filter(lambda emp:emp[2]=="IT", employees)))
print("IT department Employees:", it_people)

#Increase salary by 10% for all employees
increased_salaries = list(map(lambda emp:(emp[0], emp[1]*1.10, emp[2]), employees))
print("Employees with 10% salary increase:", increased_salaries)

#Find employees with salary >50000
high_salary_epmloyees = list(filter(lambda emp: emp[1] > 50000, employees))
print("Employees with salary > 50000:", high_salary_epmloyees)

#Extract just names and the departments
names_and_depts = list(map(lambda emp: (emp[0], emp[2]),employees))
print("Names and Departments:", names_and_depts)
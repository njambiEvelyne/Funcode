employees = [("Alice", 50000, "IT"), ("Bob", 45000, "HR"), ("Charlie", 60000, "IT")]
it_people = map(lambda x: x[2] == "IT", employees)
for k, v in employees:
  if it_people:
    names =filter(lambda n: n =="IT")
print(list(it_people))

#list_comprehension = a compact and easy way to creat lists in python other than using loops.
# [expression for value in iterable if espression]
grades = [34,79,23,85,92,87]
passing_grades = [x+1 for x in grades]
print(passing_grades)
pass_grades =[x for x in grades if x>70]
print(pass_grades)
names =["Jothsna","Jasmi","sasi","krishna"]
name =[x.upper() for x in  names]
print(name)
naam =[x[0] for x in names]
print(naam)
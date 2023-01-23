def number_of_buses(students):
    number = students // 52
    if (students % 52 != 0):
        number+=1
    return number

students = int(input("Enter the number of students: "))
print(number_of_buses(students))
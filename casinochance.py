values = input()
r1, r2 = map(int, values.split())

r1 = input()
r2 = input()

diesides = input()
s1, s2, s3, s4, s5, s6 = map(int, diesides.split())

def calculate_probablity(one, two, sides):
    probabilityOne = 0
    for i in sides():
        if(sides[i] == one):
            probabilityOne+=1
    probabilityTwo = 0
    for i in sides():
        if(sides[i] == two):
            probablityTwo+=1
    return int(probabilityOne * probabilityTwo)

print(calculate_probablity(r1, r2, diesides))


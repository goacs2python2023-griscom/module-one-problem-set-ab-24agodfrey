
values = input()
r1, r2 = values.split(" ")

diesides = input()
s1, s2, s3, s4, s5, s6 = diesides.split(" ")

def calculate_probablity(r2, r1, diesides):
    probabilityOne = 0
    probablityTwo = 0
    sides = len(diesides)
    probability_A = diesides.count(r1) / sides
    probability_B = diesides.count(r2) / sides
    return (probability_A * probability_B) * 100

print(calculate_probablity(r1, r2, diesides))




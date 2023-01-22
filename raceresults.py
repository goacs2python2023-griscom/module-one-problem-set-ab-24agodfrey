me = 8.87
one = 9.43
two = 4.57
three = 8.45


def winnings(me, one, two, three):
    number = 0
    if(me > one):
        number+=1
    if(me > two):
        number+=1
    if(me > three):
        number+=1
    if(number == 0):
        return "no medal"
    if(number == 1):
        return "bronze"
    if(number == 2):
        return "silver"
    if(number == 3):
        return "gold"

print(winnings(me, one, two, three))
    

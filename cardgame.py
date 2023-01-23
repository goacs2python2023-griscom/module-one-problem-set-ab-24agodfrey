def dad(top, bottom):
    cards = top + bottom
    if "d" in cards:
        if "a" in cards:
            if cards.count("d") >= 2:
                return "yes"
            else:
                return "no"    
        else:
            return "no"       
    else:
        return "no"
     

top = input()

bottom = input()


print(dad(top, bottom))


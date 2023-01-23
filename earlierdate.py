def compare_dates(month1, day1, year1, month2, day2, year2):
    date1 = (year1, month1, day1)
    date2 = (year2, month2, day2)
    if date1 < date2:
        return "before"
    elif date1 > date2:
        return "after"
    else:
        return "same"

month1, day1, year1, month2, day2, year2 = map(int, input("Enter month, day, and year of two dates separated by space: ").split())

print(compare_dates(month1, day1, year1, month2, day2, year2))
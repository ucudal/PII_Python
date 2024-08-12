def is_leap(year):
    return year % 4 == 0 and (not (year % 100 == 0) or year % 400 == 0)


print("2000 es bisiesto? :", is_leap(2000))

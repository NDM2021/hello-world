import math

def LeapYear(j, f):
    if j % f == 0:
        return True
    else:
        return False

print(LeapYear(2020, 4))

# Norris Mayes
# 3/9/20
# This program takes the year as parameter and divide it by 4 and check if true or false

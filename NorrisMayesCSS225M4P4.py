# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))

if year > 1900:
    input("Woah, that's the past!")
if year > 1900 & year >= 2020:
    input("That's totally the present!")
else:
    input("Far out, that's the future!!")

# Norris Mayes
# 2/11/20
# This program print based on your origin if past, present, of future

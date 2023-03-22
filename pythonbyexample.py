from math import pi, sqrt

#001
F_name = input("What is your first name ? ")
print (f"Hello, {F_name}")

#002
L_name = input("What is your Surname ? ")
print(f"How are you Mr. {F_name} {L_name}")

#003
print (" What do you call a bear with no teeth? \n A gummy bear!!!")

#004
N_1 = int(input("Enter a number "))
N_2 = int(input("Enter a number "))
ans = N_1 + N_2
print(f"The total is {ans}")

#005
N_1 = int(input("Enter a number "))
N_2 = int(input("Enter a number "))
N_3 = int(input("Enter a number "))
ans = (N_1 + N_2)* N_3
print(f"The total is {ans}")

#006
Total_Pizza = int(input("How many slices of pizza did you start with ?  "))
Eaten_Pizza = int(input("How many slices did you eat ? "))
Remaining_Pizza = Total_Pizza - Eaten_Pizza
print (f"You have {Remaining_Pizza} slices of pizza left")

#007
age = int(input("How old are you ?  "))
newAge = age + 1
fullName = L_name + " " + F_name
print (f"Mr. {fullName} Goodday, you will be {newAge} by next year")

#008
Total_price = int(input("What is your total bill ? "))
number_of_persons = int(input("How many people ate the food ? "))
individual_bill = Total_price // number_of_persons
print (f"Each person must pay {individual_bill} dollars each")

#009
days = int(input("Number of days  :  "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print (f"{days} days = {hours} hours = {minutes} minutes = {seconds} seconds")

#010
kilo = int(input("How much kilo do you want to convert to pounds : "))
pounds = 2204 * kilo
print(f"{kilo} kilos is equal to {pounds} pounds")

#011
X = int(input("Enter a number over 100 :  "))
Y = int(input("Enter a number below 10 :  "))
Z = X / Y
print (f"{Y} goes into {X}, {Z} times")

#012
x = int(input("Enter a number 1: "))
y = int(input("Enter a number 2: "))
if x > y:
    print(f"{y} and {x}")
else:
    print(f"{x} and {y}")

#013
z = int(input("Enter a number below 20 : "))
if z >= 20:
    print("Too high")
else:
    print("Thank you")

#014
q = int(input("Enter a number between 10 and 20"))
if q > 10 and q <= 20:
    print("Thank you")
else:
    print("Incorrect answer!")

#015
color = input("What is your favourite ?  ")
color = color.lower()
if color == "red":
    print("I love red too")
else:
    print(f"i don't like {color}, I prefer red")

#016
wtr = input("""
    Answer Yes or No:
    Is it raining?
            """).lower()
if wtr == "yes":
    htr = input("Is it windy?").lower()
    if htr == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an Umbrella")
else:
    print("Enjoy your day")

#017
f = int(input("How old are you ?  "))
if f >= 18:
    print("you can vote")
elif f == 17:
    print("You can learn to drive")
elif f == 16:
    print("You can buy a lottery ticket")
else:
    print("You can go Trick-or-Treating")

#018
num = int(input("Enter a number  :  "))
if num < 10:
    print("Too low")
elif num >= 10 and num <= 20:
    print("Correct")
else:
    print("Too High")

#019
num = int(input(""" Please enter 1, 2, or 3  :   """))
if num == 1:
    print("Thank You")
elif num == 2:
    print("Welldone")
elif num == 3:
    print("Correct")
else:
    print("Error Message")

#020
full_name = input("What is your fullname :  ")
full_name = len(full_name)
print(full_name)

#021
firstName = input("What is your frstname : ")
lastName = input("What is your lastname : ")
fullName = firstName + " " + lastName
length = len(fullName)
print(f"{fullName} is {length} chars long")

#022
firstname = input("What is your firstname : ").title()
lastname = input("What is your lastname : ").title()
fullname = lastname + " " + firstname
print(fullname)

#023
nurse = input("Enter a line from a nursery rhyme :  ")
length = len(nurse)
print(length)
start_num = int (input ("Enter a starting number : "))
stop_num = int (input ("Enter a stopping number : "))
new_nurse = nurse[start_num : stop_num]
print(new_nurse)

#024
word = input("Type any sentence :  ").upper()
print(word)

#025
first = input("What is your firstname :  ")
length_first = len(first)
if length_first < 5:
    second = input("What is your lastname :  ")
    full = first + second
    print(full.upper())
else:
    print(first.lower())

#026
word = input("Enter a word :  ").lower()
rest = len(word)
first = word[0]
if  first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    new = word[1 : rest]
    new_new = new + first + "ay"
    print(new_new)
else:
    new_new = word + "way"
    print(new_new)

#027
Num_1 = float(input("Enter a number with many decimal places : "))
ans = Num_1 * 2
print(ans)

#028
ans = round(ans, 2)
print (ans)

#029
Num_2 = int(input("Enter another number over 500 : "))
ans = sqrt(Num_2)
ans = round(ans, 2)
print(ans)

#030
ans = pi
ans = round(ans, 5)
print(ans)

#031
radius = int(input("Enter the radius of a circle :  "))
area = pi * (radius**2)
ans = round(area, 2)
print(ans)

#032
radius = int(input("Enter the radius of a circle :  "))
depth = int(input("Enter the depth of a cylindar :  "))
area = pi * (radius**2)
total_volume = area * depth
ans = round(total_volume, 3)
print(ans)

#033
num_2 = int(input("Enter the Divisor:  "))
num_1 = int(input("Enter the Divided :  "))

division = num_1 // num_2
modulo = num_1 % num_2

print(f"{num_1} divided by {num_2} is {division} remaining {modulo}")

#034
print("""
    1) Square
    2) Triangle

    Enter a number:
    """)
X = int(input("Select from the menu :  "))
if X == 1:
    Y = int(input("Enter the value of a side :  "))
    areaOfSquare = Y * Y
    print(f"The area of the square is {areaOfSquare}")
elif X == 2:
    Y = int(input("Enter the height of the Triangle :  "))
    Z = int(input("Enter the base of the Triangle :  "))
    areaOfTriangle = (Y * Z) / 2
    print(f"The area of the Traingle is {areaOfTriangle}")
else:
    print("Invalid Entry!")

#035
num = 0
name = input("Enter your name :  ")
for num in range (0, 3):
    print(name)
    num += 1






























#My exclusives
#001
text = input("Enter text here: ").lower()
space = " "
words = 0

for char in text:
    if char is space:
        words = words + 1


words = words + 1
print(f"""

        There are {words} words in your sentence!
        
        """)

#002
def calculate(operator, operand1, operand2):
  if operator == "+":
    return operand1 + operand2
  elif operator == "-":
    return operand1 - operand2
  elif operator == "*":
    return operand1 * operand2
  elif operator == "/":
    if operand2 == 0:
      print("Invalid denominator")
    else:
      return operand1 / operand2

print("Welcome to the calculator! Enter 'exit' to quit.")

while True:
  operator = input("Enter an operator (+, -, *, /): ").lower()
  if operator == "exit":
    break
  
  operand1 = int(input("Enter the first operand: "))
  operand2 = int(input("Enter the second operand: "))
  
  result = calculate(operator, operand1, operand2)
  print(f"{operand1} {operator} {operand2} = {result}")

#003
import random

def generate_poem():
  nouns = ["love", "heart", "eyes", "smile", "happiness", "joy"]
  verbs = ["cherish", "adore", "love", "appreciate", "admire", "respect"]
  adjectives = ["beautiful", "gorgeous", "wonderful", "amazing", "magnificent", "stunning"]

  noun = random.choice(nouns)
  verb = random.choice(verbs)
  adjective = random.choice(adjectives)

  poem = f"My {noun} for you grows stronger every day,\n"
  poem += f"I {verb} and {verb} you in every single way.\n"
  poem += f"Your {adjective} face and {adjective} smile,\n"
  poem += f"Fills my {noun} with love and {noun} all the while."

  return poem

print(generate_poem())

#004
from cmath import pi
import turtle
bob = turtle.Turtle()

def square(t, length):
    for i in range (4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    for i in range (n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    circumference = 2 * pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)

circle(bob, 200)
square(bob, 250)
polygon(bob, 5, 100)

turtle.mainloop()

#005
plus = (" + ")
pipe = (" | ")
hyph = (" - ")
spc = ("   ")
space = (" ")

top = plus + hyph + hyph + hyph + hyph + plus + hyph + hyph + hyph + hyph + plus 
bot =  pipe + spc + spc + spc + spc + pipe + spc + spc + spc + spc + pipe

def Top():
    print(top)

def Bott():
    print(bot)

def draw ():
    Top()
    Bott()
    Bott()
    Bott()
    Bott()
    Top()
    Bott()
    Bott()
    Bott()
    Bott()
    Top()


draw()

#006
from cmath import pi
import turtle

bob = turtle.Turtle()


def arc(t, r, angle):
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

for i in range (3):
    arc(bob, 150, 360)

turtle.mainloop()
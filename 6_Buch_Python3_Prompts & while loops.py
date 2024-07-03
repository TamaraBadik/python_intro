#5_Buch_Python3_Crashcourse
#Function input()
#Your programs can prompt the user for input. All input is stored as a string.
#Prompting for a value
# in CSV

'''
message = input("Tell me something and I will repeat it back to you:")
print(message)

name = input("Please enter your name: ")
print(f"Hello, {name}!")

#in case the message/ the string consists of more than one line => use +=
prompt = "If you tell us who you are, we can personalize ths messages you see."
prompt += "\nWhat's your first name?"
name = input(prompt)
print(f"\nHello, {name}!")

#Prompting for numerical input
#input() interprets everything as a string: could be a problem, if we need the 
#input, such as to define the age: 
'''
'''
>>> age = input("How old are you? ")
How old are you? 16
>>> age
'16'
>>> age >= 18
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>=' not supported between instances of 'str' and 'int'
'''
#function int(): if we want to use the numbers for calculations or comparisons:
'''
>>> age = input("How old are you? ")
How old are you? 16
>>> age = int(age)
>>> age >= 18
False
>>>
'''
'''
>>> hight = input("How tall are you, in inches? ")
How tall are you, in inches? 55
>>> hight = int(hight)
>>> if hight >= 48:
...     print("\nYou're tall enough to ride!")
... else:
...     print("You will be able to ride, when you are a little older.")
...

You're tall enough to ride!
'''
# Modulo-operator(%) 
'''
>>> number = input("Enter a number, and I'll tell you if it's even or odd: ")
Enter a number, and I'll tell you if it's even or odd: 34
>>> number = int(number)
>>>
>>> if number % 2 == 0:
...     print(f"\nThe number {number} is even.")
... else:
...     print(f"\nThe number {number} is odd.")
...

The number 34 is even.
>>>
'''
#7-1: Rental Car
'''
message = input("What kind of car would you like? ")
print(f"Let me see if I can find you a {message.title()}.")

Let me see if I can find you a BMW.
>>>'''
#7-2: Restaurant Seating
'''
message = input("How many people are in your dinner party tonight? ")
message = int(message)

if message >= 8:
    print("\nI'm sorry, you'll have to wait for a table.")
else:
    print("We have a free table for you!")

#7-3: Multiples of Ten
message = input("Give me a number, please: ")
number = int(message)

if number % 10 == 0:
    print(f"\n{number} is a multiple of 10.") 
else:
    print(f"{number} is not a multiple of 10.")
'''
''''
28 is not a multiple of 10.
>>>
...

20 is a multiple of 10.
>>>
'''
#While loops
#A while loop repeats a block of code as long as a certain condition is true.
#A simple while loop
'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number+=1
'''
#Letting the user choose when to quit
'''
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "Enter 'quit' to end the programm. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "Enter 'quit' to end the programm. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit': #to avoid the outcome 'quit'
        print(message)
'''
#Flags: when we have a a series of prompts
'''
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "Enter 'quit' to end the programm. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
'''
#Using break to exit a loop
'''
prompt = "\nPlease enter the name of the city you have visited:"
prompt += "\n(Enter 'quit' when you are finished:) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
'''
#You can use the break statement and the continue #statement with any of 
# Python's loops. For example you can use break to quit a for loop that's 
# working through a list or a dictionary. You can use continue to skip over 
# certain items when looping through a list or dictionary as well.

#Using continue in a loop
current_number = 0
while current_number <10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

banned_users = ['eve', 'fred', 'gary', 'helen']

prompt = "\nAdd a player to your team."
prompt += "\nEnter 'quit' when you're done. "

players = []
while True:
    player = input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print(f"{player} is banned!")
        continue
    else:
        players.append(player)

print("\nYour team:")
for player in players:
    print(player)

#Avoiding infinite loops
#Every while loop needs a way to stop running so it won't
#continue to run forever. If there's no way for the condition to
#become False, the loop will never stop running. You can
#usually press Ctrl-C to stop an infinite loop.

#An infinite loop
'''
while True:
    name = input("\nWho are you? ")
    print(f"Nice to meet you, {name.title()}!")
'''
x = 1
while x <= 5:
    print(x)
    x += 1 #without this line the loops goes infinite.

#7-4: Pizza Toppings
prompt = "\nWhat topping would you like on your pizza? "
prompt += "Enter 'quit' when you are finished: "
while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
    else: 
        break

#7-5: Movie Tickets
prompt = "\nHow old are you? "
prompt += "Enter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    
    if age < 3:
        print(" You get in free!")
    elif age < 13:
        print(f" Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

#Moving elements from one list to another:
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"\nVarifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    print(f"\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
        
#Removing all instances of a value from a list
#The remove() method removes a specific value from a list,
#but it only removes the first instance of the value you
#provide. You can use a while loop to remove all instances
#of a particular value.
#Removing all cats from a list of pets
pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    print(pets)

# filling a dictionary
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person to respond? (yes/no) ")
    if repeat == 'no' :
        polling_active = False
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name.title()} would like to climb {response.title()}.")




##7-8: Deli

#Make a list called sandwich_orders and fill it with the names of various 
# sandwiches. Then make an empty list called finished_sandwiches. Loop through 
# the list of sandwich orders and print a message for each order, such as I 
# made your tuna sandwich. As each sandwich is made, move it to the list of 
# finished sandwiches. After all the sandwiches have been made, print a message 
# listing each sandwich that was made.
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print(f"\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich")

#7-9: No Pastrami

#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 
# pastrami' appears in the list at least three times. Add code near the 
# beginning of your program to print a message saying the deli has run out of 
# pastrami, and then use a while loop to remove all occurences of 'pastrami' 
# from sandwich_orders. Make sure no pastrami sandwiches end up in 
# finished_sandiches.

sandwich_orders = [
    'veggie', 'pastrami', 'grilled cheese', 'turkey', 'pastrami', 'roast beef', 
    'pastrami']
finished_sandwiches = []

print("I am sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders: 
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")

#7-10: Dream Vacation

#Write a program that polls users about their dream vacation. 

name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "
responses = {}
while True:
    name = input(name_prompt)
    place = input(place_prompt)
    responses[name] = place
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break
    print("\n--- Results ---")
    for name, place in responses.items():
        print(f"{name.title()} would like to visit {place.title()}.")

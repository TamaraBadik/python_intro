# Variable types
number = 32 # declare integer/number variable with name number and value 32
name = "Tamara" # declare a string variable with name `name` with value "Tamara"
# print(number * 15) # correct caculation with type number/integer
# print(name.upper()) # correct usage of string method

#print(name + 2) # wrong because make mathematical operation with type string
#print(number.upper()) # wrong because try to uppercase a number

loggedIn = False # boolean variable type - just has two states: True or False

user = ["Tamara", "Tommy", "Mary", "John"] # a basic list (array). Index 0 based
#print(user) # prints the list
#print(user[0]) # access first (zero index) person in user array
#print(user[3]) # access 4th person in human language - position/index 3

#print(user[:3]) # array slicing everything until third index
#print(user[1:]) # array slicing kick out first person
selectedUser = user[:2] # slice user and write into new variable
#print(selectedUser) # print the 

# objects = complex data structutre
shoppingCart = {
    "totalPrice": 1249,
    "seperatePrices": [23, 56, 983],
    "items": ["Bottle", "Table", "gold necklace"],
    "userId": "84bdr567",
    "trackingObject": {
        "trackigId": 2813979218
    }
}

address = {
    "street": "vulkanstrasse",
    "zip": 19023
}
#print(shoppingCart)
#print(address)

# conditionals (if/else, elseif - when this than that)
age = 332 # variable assignment
if age > 17: 
    print ("old enough")
elif age == 22: # variable comparision
    print("hey you are same age than me")
else: 
    print ("too young")

# loops 

userAges = [32, 41, 44, 12, 11, 5, 8, 99,] # camel case variable

for age in userAges:
    print("Firstloop iteration:", age)

user_ages = [32, 41, 44, 12]

for age in user_ages:
    print("secondloop iteration: ")

    print(age)
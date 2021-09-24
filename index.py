# Variable types
number = 32 # declare integer/number variable with name number and value 32
name = "Tamara" # declare a string variable with name `name` with value "Tamara"
print(number * 15) # correct caculation with type number/integer
print(name.upper()) # correct usage of string method

#print(name + 2) # wrong because make mathematical operation with type string
#print(number.upper()) # wrong because try to uppercase a number

loggedIn = False # boolean variable type - just has two states: True or False

user = ["Tamara", "Tommy", "Mary", "John"] # a basic list (array). Index 0 based
print(user) # prints the list
print(user[0]) # access first (zero index) person in user array
print(user[3]) # access 4th person in human language - position/index 3

print(user[:3]) # array slicing everything until third index
print(user[1:]) # array slicing kick out first person
selectedUser = user[:2] # slice user and write into new variable
print(selectedUser) # print the 

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
print(shoppingCart)
print(address)

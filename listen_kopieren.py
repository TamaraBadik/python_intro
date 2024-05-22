#Listen kopieren
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy new friend's favorite foods are:")
print(my_foods)
friends_food = my_foods[:]
my_foods.append('canolli')
friends_food.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy frind's favorite foods are:")
print(friends_food)
#dies funktioniert nicht als kopieren sondern als wird auf der gleichen Liste 
# zugewiesen:
friends_food = my_foods #ohne [:] funktioniert nicht: bei kopieren einer Liste 
            #muss man nur drauf achten, dass das mithilfe eines Slices erfolgt.
#Übungen
my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream', 'nudels', 'tee']
print("\nThe first three items in the list are:")
print(my_foods[:3])
print("\nThe items from the middle of the list are:")
print(my_foods[2:-1])
print("\nThe last three items in my list are:")
print(my_foods[-3:])
fav_pizzas = ['pepperony' , 'margarita' , 'tony']
friend_pizzas = fav_pizzas[:]
fav_pizzas.append('meat')
friend_pizzas.append('ananas')
print("\nMy favorite pizzas are:")
print(fav_pizzas)
print("\My friend's favorite pizzas are:")
print(friend_pizzas)
print("\nMy favorite pizzas are:")
for pizza in fav_pizzas:
    print(f"- {pizza}")
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
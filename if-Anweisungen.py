#Buch_Python3
#Chapter5: if-Anweisungen
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
for car in cars:
    if car =="bmw":
        print(car.upper())
    else:
        print(car.title())
#if als Bedingung-> true oder false
'''
>>> car = 'bmw'
>>> car == 'bmw'
True
>>> car == 'audi'
False
>>> car = 'audi'
>>> car == 'Audi'
False
>>> car.lower() == 'audi' #eine Prüfung unabhängig von der Groß- und 
                            Kleinbuchstaben                            
True
>>>
>>> car = 'Audi'
>>> car.lower() == 'audi'
True
>>> car
'Audi'
>>> #die Funktion ändert nicht den in car gespeicherten Wert. 
'''
#!= -> not equal 
#wenn es sinnvoll ist, auf Ungleichheit zu prüfen
requested_topping = 'Mashrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')
#nummerische Vergleiche
'''>>> age = 18
>>> age == 18
True
>>> age != 18
False
>>> age = 18
>>> age ==17
False
'''
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again.")
#in if-Anweisungen können jegliche mathematischen Vergleiche verwendet werden:
'''>>> age = 88
>>> age < 17
False
>>> age > 17
True
>>> age >= 17
True
>>>
'''
##Prüfung auf mehrere Bedingungen
#mit "and"
'''
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >=21
False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
>>>
'''
#or -> wenn mindestens eine der Teilbedingungen wahr ist
'''
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 22 or age_1 != 18
True
>>> age_0 < 22 or age_1 !=18
False
>>>'''
#Prüfung auf Vorhandensein eines Werts in einer Liste:
#Schlüsselwort "in"
'''
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
>>>
'''
##Prüfung auf Abwesenheit eines Wertes in einer Liste 
#Schlusselwort "not"
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"\n\t{user.title()}, you can post a response if you wish.")
#boolesche Ausdrücke => eine andere Bezeichung für eine Bedingung
#die Werte "true" und "false" werden auch als 'boolische Werte' bezeichnet. 
#Übungen
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False")
print(car == 'audi')
flower = 'orchidee'
print("\nIs flower == 'orchidee'? I predict True.")
print(flower == 'orchidee')
print("\nIs flower == 'kaktus'? I predict False")
print(flower == 'kaktus')
flower = 'lily of the valley'
print("\nIs flower == 'lily of the valley'? I predict True.")
print(flower == 'lily of the valley')
print("\nIs flower == 'lily'? I predict False")
print(flower == 'lily')
flower = 'tulip'
print("\nIs flower == 'tulip'? I predict True.")
print(flower == 'tulip')
print("\nIs flower == 'begonia'? I predict False")
print(flower == 'begonia')
flower = 'violet'
print("\nIs flower == 'violet'? I predict True.")
print(flower == 'violet')
print("\nIs flower == 'carnation'? I predict False")
print(flower == 'carnation')
cars = ['bmw' , 'AUDI' , 'toyota' , 'subaru']
for car in cars:
    if car =="AUDI":
        print(car.lower())
    else:
        print(car.title())
for car in cars:
    if car != 'AUDI':
        print(car.title())
    else:
        print(car.lower())
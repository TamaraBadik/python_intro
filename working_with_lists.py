###4. Mit Listen arbeiten
magicians = ['alice' , 'david' , 'carolina']
for magician in magicians:
    print(magician)
magicians = ['alice' , 'david' , 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you everyone. That was a great magic show!")
#Übungen:
pizzas = 'pepperony' , 'margarita' , 'tony'
for pizza in pizzas: 
    print(f"I like {pizza.title()}.")
print("\nI really like pizza!")
dogs = "bulldog" , 'schaefer' , 'hund'
for dog in dogs: 
    print(f"A {dog.title()} would make a great pet.")
print('\nAny of those anymals would make a great pet.')
##Nummerische Listen
# die Funktion range() beginnt bei dem ersten angegebenen Wert zu zählen und 
# hört bei dem zweiten Wert auf, sodass dieser Endwert nicht in der Ausgabe 
# erhalten ist. 
for value in range(1, 5):
    print(value)
#um die Zahlen 1 bis 5 auszugeben, müss range(1, 6) verwendet werden.
for value in range(1, 6):
    print(value)
# es ist auch möglich, range() nur ein einziges Argument zu übergeben. In dem 
# Fall beginnt die Zahlenfolge bei 0.
for value in range(6):
    print(value)
#mit list() kann man die Folge zu einer Liste machen:
numbers = list(range(1, 6))
print(numbers)
#mit range() kann man manche Zahlen in dem Bereich auslassen.
#z.B. nur die gerade Zaheln ausgeben:
even_numbers = list(range(2, 14, 2))
print(even_numbers)
#eine Liste die ersten zehn Quadratzahlen
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
#to condense the code:
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
#'Einfache Statistiken f. nummerische Listen
#den kleinsten (min) und den größten(max) Wert sowie die Summe (sum) in einer 
# Liste schnell herausfinden:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
##Listennotation
quadrats = [value**2 for value in range(1, 11)]
for quadrat in quadrats: 
    print(quadrat) 
#oder 
quadrats = [value**2 for value in range(1, 11)]
print(quadrats) # Unterschied, dass hier die Ausgabe sieht aus wie eine Liste: 
    #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#Übungen
for value in range(1, 21):
    print(value)
for value in range (1, 100):
    print(value)
numbers = list(range(1, 8))
print(numbers)
numbers = list(range(0, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
uneven_numbers = list(range(1, 20, 2)) # here at the end wird addierd 1+2, so if
    #I write (1, 20, 3) it will add 3 to the next number
print(uneven_numbers)
trees = list(range(3, 31, 3))
for number in trees: 
    print(number)

cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
for cube in cubes:
    print(cube)

cubes = [value**3 for value in range(1, 11)]
print(cubes)
#oder
cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)

##Slices erstellen
players = ['charles' , 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
players = ['charles' , 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
#wenn man den 1. Index in einem Slice weglässt, beginnt Python authomatisch am 
# Anfang der List:
print(players[:3])
print(players[2:])
#beliebige Slices vom Ende der Liste aus abrufen:
print(players[-2:]) 
#Slice in for Schleife 
print('Here are the first tree players of my team:')
for player in players[:3]:
    print(player.title())




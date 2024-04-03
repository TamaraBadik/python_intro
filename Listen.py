#####2. Buch Eric Matthes 
#2. Einführung in Listen
#eine Liste => geordnete Sammlung von Elementen. Darstellung durch eckige 
# Klammern und Trennung durch Kommas. 
bicycles = ['trek', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[0].upper())
#um auf das letzte Element einer Liste zurückzugreifen => "-1", Index "-2" etc
# ist auch möglich.
print(bicycles[-1].title())
#in einem Satz einzelne Elemente aufzubauen
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
#Ubungen
my_friends = ['mariam', 'lili', 'tatev', 'micha', 'christian', 'christine', 
"bianca"]
print(my_friends[-2].upper())
message = f'Hallo, {my_friends[2].title()}. I said, "Hallo!".'
print(message)

##Elemente in einer Liste ändern/replace
motocycles = ["honda" , 'yamaha', "suzuki"]
motocycles[0] = 'ducati'
print(motocycles)
##Elemente zu einer Liste hinzufügen
#am Ende einer Liste
motocycles = ["honda" , 'yamaha', "suzuki"]
motocycles.append('ducati')
print(motocycles)
#man kann auch mit einer leere Liste anfangen
motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')
print(motocycles)
#Methode "insert" -> ein einer beliebigen Stelle neues Element einfügen
motocycles = ["honda" , 'yamaha', "suzuki"]
motocycles.insert(0, 'ducati')
print(motocycles)
##Elemente aus einer Liste entfernen
motocycles = ["honda" , 'yamaha', "suzuki"]
del motocycles[0]
print(motocycles)
#deletes permanenty
# wenn man ein Wert (letzte in der Liste) nach dem entfernen noch verwenden 
# möchte, jedoch den entfernten Wert weiterhin nutzen möchte-> "pop()" Methode
# z.B. aus der Liste der aktiven mitglieder herausnehmen aber zur Liste der 
# inaktiven hinzufügen
motocycles = ["honda" , 'yamaha', "suzuki"]
popped_motocycle = motocycles.pop()
print(motocycles)
print(popped_motocycle)
#mit der Methode kann man eine Aussage über in chronologische Reihnfolge 
# geordnete Daten machen
motocycles = ["honda" , 'yamaha', "suzuki"]
last_owned = motocycles.pop()
print("The last motocycle I owned was a " + last_owned.title() + ".")
#mit "pop()" Elemente von beliebigen Stellen entfernen
motocycles = ["honda" , 'yamaha', "suzuki"]
first_owned = motocycles.pop(-1)
print(f"The first motocycle I owned was a  {first_owned.title()} .")
#wenn man ein Element entfernen möchte, deren Position man nicht weißt->Methode 
# "remove()"
motocycles = ["honda" , 'yamaha', "suzuki", "ducati"]
motocycles.remove('ducati')
print(motocycles)
#Bei der Methode "remove()" gibt's eine Möglichkeit mit dem entfernten Wert 
# weiterzuarbeiten
motocycles = ["honda" , 'yamaha', "suzuki", "ducati"]
too_expensive = "ducati"
motocycles.remove(too_expensive)
print(motocycles)
print(f"\nA {too_expensive.title()} ist too expensive for me.")
#Übungen
List_of__the_guests = ["Miqayel", "Mariam", "Lili"]
print(List_of__the_guests[1])
List_of__the_guests [1] = "Karine"
print(List_of__the_guests)
print(f"Hey {List_of__the_guests[0]}, you are welcome!")
print(f"Hey {List_of__the_guests[1]}, you are welcome!")
print(f"Hey {List_of__the_guests[2]}, you are welcome!")
print(f"Hey {List_of__the_guests}, I have found a bigger table.")
List_of__the_guests.insert(0, "Hayk")
List_of__the_guests.insert(2, 'Kolja')
print(List_of__the_guests)
List_of__the_guests.insert(5, 'Mariam')
print(List_of__the_guests)
print(f"Dear {List_of__the_guests}, I can invite only two people.")
List_of__the_guests.pop(1)
print(List_of__the_guests)
popped_1_guest ='Hayk'
print(f"Dear {popped_1_guest}, I am sorry, but I can't invite you.")
List_of__the_guests.pop(0)
print(List_of__the_guests)
popped_2_guest = List_of__the_guests.pop()
print(popped_2_guest)
print("Dear " + popped_2_guest + " sorry!")
print(List_of__the_guests)
print(len(List_of__the_guests))
popped_3_guest = List_of__the_guests.pop(0)
print(popped_3_guest)
print(f"Dear " + popped_3_guest + " sorry, I can't invite you!")
print(f"Dear {List_of__the_guests} I am still expecting you.")
del List_of__the_guests[0 :] 
print(List_of__the_guests)
print(len(List_of__the_guests))

##Listen Ordnen
#Listen mit sort() dauerhaft alphabetisch sortieren. Dabei nicht möglich zur 
# ursprünglichen Sortierung zurückzukehren.
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
cars.sort()
print(cars)
#für umgekehrte alphabetische Reihnfolge (dauerhaft)
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
cars.sort(reverse=True)
print(cars)
#Listen mit sorted() temporary sortieren
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the sorted lost again:")
print(sorted(cars, reverse=True))
#reverse() ist keine umgekährte alphabetische Sortierung vornimmt, sondern 
# einfach die ursprüngliche Reihnfolge der Liste. Dabei die Änderungen sind 
# permanent. Aber kann man ändern, indem man nochmals reverse() verwendet
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
print(cars)
cars.reverse()
print(cars)
##Die Länge einer Liste ermitteln
#Function len()
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
print(len(cars)) #oder gleich im Terminal ausgeben
#Übungen
travel_destinations = ['japan', 'armenia' , 'iran' , 'norway']
print(travel_destinations)
print(sorted(travel_destinations))

sorted(travel_destinations)
travel_destinations.reverse()
print(travel_destinations)
print(travel_destinations[-1]) #letzer Wert
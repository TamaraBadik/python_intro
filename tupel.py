###Tupel -> Listen, die unveränderbar sein sollen; mit runde Klammern
#im Vergleich zu Listen sind Tupel einfache Datenstrukturen. Zu verwenden, wenn
# die Werte im Programmverlauf nicht verändert werden sollen.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#nicht möglich -> dimensions[0] = 250
#technisch werden Tupel durch das Vorhandensein eines Kommas definiert.
# Wenn man ein Tupel nur mit einem Element definieren will, muss man ein
# nachfolgendes Komma angeben:
my_t = (3, )
print(my_t)
#for Schleife mit Tupel
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
#Tupel überschreiben
dimensions = (200, 50)
print("Orinignal dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
#Übungen
menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )
print("Today's menu:")
for item in menu_items:
    print(f"-{item.title()}")

# wird nicht funktionieren: menu_items[1] = "salami"
#print(menu_items)

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
    )
print("\nOur menu has been updated.")
print("\nYou can now choose from the following items:")
for item in menu_items:
    print(f"- {item.title()}")
"""Notizen: PEP 8-> Python enhancement proposal;
79 Zeichnen pro Zeile
https://www.python.org/dev/peps/pep-0008/:
code is read much more often than it is written.
"""
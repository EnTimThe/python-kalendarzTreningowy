


planTreningowy = {}

stop = input("Czy chcesz dodać nowe ćwiczenie (y/n)? ")

while stop == "y":
    nrCwiczenia = input("Podaj nr ćwiczenia: ")
    planTreningowy.update({nrCwiczenia: {}})
    nazwaCwiczenia = input("Podaj nazwę ćwiczenia: ")
    planTreningowy[nrCwiczenia].update({"nazwa ćwiczenia:": nazwaCwiczenia})
    iloscSerii = input("Podaj ilość serii: ")
    planTreningowy[nrCwiczenia].update({"ilość serii:": iloscSerii})
    iloscPowtorzen = input("Podaj ilość powtórzeń w serii: ")
    planTreningowy[nrCwiczenia].update({"ilość powtórzen:": iloscPowtorzen})
    stop = input("Czy chcesz dodać następne ćwiczenie (y/n)? ")

print("\n")

for id, dictionary in planTreningowy.items():
    print("nr ćwiczenia " + id)
    for key in dictionary:
        print(key, dictionary[key])

print("\n")

edycjaPlanu = int(input(
    "Czy chcesz: 1. Wyświetlić ćwiczenie? 2. Usunąć ćwiczenie? 3. Dodać ćwiczenie? 4. Pominąć ten krok? (Podaj odpowiedni nr.) "))
while edycjaPlanu == 1 or 2 or 3:
    if edycjaPlanu == 1:
        wyswietlCwiczenie = input("Podaj nr ćwiczenia: ")
        print(planTreningowy[nrCwiczenia])
        edycjaPlanu = int(input(
            "Czy chcesz: 1. Wyświetlić ćwiczenie? 2. Usunąć ćwiczenie? 3. Dodać ćwiczenie? 4. Pominąć ten krok? (Podaj odpowiedni nr.) "))
    elif edycjaPlanu == 2:
        usunCwiczenie = input("Podaj nr ćwiczenia: ")
        planTreningowy.pop(usunCwiczenie)
        edycjaPlanu = int(input(
            "Czy chcesz: 1. Wyświetlić ćwiczenie? 2. Usunąć ćwiczenie? 3. Dodać ćwiczenie? 4. Pominąć ten krok? (Podaj odpowiedni nr.) "))
    elif edycjaPlanu == 3:
        nrCwiczenia = input("Podaj nr ćwiczenia: ")
        planTreningowy.update({nrCwiczenia: {}})
        nazwaCwiczenia = input("Podaj nazwę ćwiczenia: ")
        planTreningowy[nrCwiczenia].update(
            {"nazwa ćwiczenia:": nazwaCwiczenia})
        iloscSerii = input("Podaj ilość serii: ")
        planTreningowy[nrCwiczenia].update({"ilość serii:": iloscSerii})
        iloscPowtorzen = input("Podaj ilość powtórzeń: ")
        planTreningowy[nrCwiczenia].update(
            {"ilość powtórzen:": iloscPowtorzen})
        edycjaPlanu = int(input(
            "Czy chcesz: 1. Wyświetlić ćwiczenie? 2. Usunąć ćwiczenie? 3. Dodać ćwiczenie? 4. Pominąć ten krok? (Podaj odpowiedni nr.) "))
    else:
        print("Plan został zmodyfikowany")
        break
    
print("\n")

print("Tak wygląda twój plan końcowy. Owocnych treningów!")

print("\n")

for id, dictionary in planTreningowy.items():
    print("nr ćwiczenia " + id)
    for key in dictionary:
        print(key, dictionary[key])



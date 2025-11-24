ukoly = []

def hlavni_menu():
    while True:
        print("Hlavní Menu:")
        print("1 - Přidat nový úkol")
        print("2 - Zobrazit všechny úkoly")
        print("3 - Odstranit úkol")
        print("4 - Konec programu\n")

        volba = input("Vyberte možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Ukončuji program. Nashledanou!")
            break
        else:
            print("Neplatná volba, zkuste to znovu.\n")

def pridat_ukol():
    nazev = input("Zadejte název úkolu: ")
    if nazev.strip():
        ukoly.append(nazev)
        print(f"Úkol '{nazev}' byl přidán.\n")
    else:
        print("Název úkolu nemůže být prázdný.\n")

def zobrazit_ukoly():
    if not ukoly:
        print("Žádné úkoly k zobrazení.\n")
    else:
        print("Seznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol}")
        print()

def odstranit_ukol():
    zobrazit_ukoly()
    if ukoly:
        try:
            cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= cislo <= len(ukoly):
                odstraneny = ukoly.pop(cislo - 1)
                print(f"Úkol '{odstraneny}' byl odstraněn.\n")
            else:
                print("Neplatné číslo úkolu.\n")
        except ValueError:
            print("Zadejte platné číslo.\n")

hlavni_menu()
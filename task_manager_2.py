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
    nazev = input("Zadejte název úkolu: ").strip()

    if not nazev:
        print("Název úkolu nemůže být prázdný.\n")
        return

    popis = input("Zadejte popis úkolu: ").strip()

    ukol = {
        "nazev": nazev,
        "popis": popis
    }

    ukoly.append(ukol)
    print(f"Úkol '{nazev}' byl přidán.\n")


def zobrazit_ukoly():
    if not ukoly:
        print("Žádné úkoly k zobrazení.\n")
    else:
        print("Seznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol['nazev']} – {ukol['popis']}")
        print()


def odstranit_ukol():
    if not ukoly:
        print("Neexistují žádné úkoly k odstranění.\n")
        return

    zobrazit_ukoly()

    try:
        cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        if 1 <= cislo <= len(ukoly):
            odstraneny = ukoly.pop(cislo - 1)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.\n")
        else:
            print("Neplatné číslo úkolu.\n")
    except ValueError:
        print("Zadejte platné číslo.\n")


hlavni_menu()
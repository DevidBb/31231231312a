

# Чтение вопросов и ответов из файла
küsimused_vastused = {}
file_path = input("Palun sisestage faili tee, kus asuvad küsimused ja vastused: ").strip()

while not os.path.exists(file_path):
    print("Viga: Faili ei leitud. Palun kontrollige tee ja proovige uuesti.")
    file_path = input("Palun sisestage faili tee, kus asuvad küsimused ja vastused: ").strip()

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        küsimus, vastus = line.strip().split(":")
        küsimused_vastused[küsimus.strip()] = vastus.strip()

# Главный цикл программы
while True:
    print("\n1. Tutvu küsimuste ja vastustega")
    print("2. Täida ankeet")
    print("3. Lisa uus küsimus ja vastus")
    print("4. Näita edukalt ankeedi täitnud isikuid")
    print("5. Välju programmist")
    valik = input("Palun vali tegevus (1-5): ").strip()
    
    if valik == "1":
        print("Küsimused ja vastused:")
        for küsimus, vastus in küsimused_vastused.items():
            print(f"Küsimus: {küsimus} | Vastus: {vastus}")
    elif valik == "2":
        nimi = input("Palun sisestage oma nimi: ").strip().capitalize()
        punktid = 0
        for küsimus, vastus in küsimused_vastused.items():
            kasutaja_vastus = input(f"Tere, {nimi}! Palun vastake järgmisele küsimusele: {küsimus}\nVastus: ").strip().lower()
            if kasutaja_vastus == vastus.lower():
                punktid += 1
        küsimuste_arv = len(küsimused_vastused)
        if punktid >= küsimuste_arv / 2:
            with open("oiged.txt", "a", encoding="utf-8") as file:
                file.write(f"{nimi}: {punktid}\n")
        else:
            with open("valed.txt", "a", encoding="utf-8") as file:
                file.write(f"{nimi}: {punktid}\n")
    elif valik == "3":
        küsimus = input("Palun sisestage uus küsimus: ").strip()
        vastus = input("Palun sisestage sellele küsimusele vastus: ").strip()
        küsimused_vastused[küsimus] = vastus
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"{küsimus}: {vastus}\n")
        print("Uus küsimus ja vastus on lisatud!")
    elif valik == "4":
        print("Edukalt ankeedi täitnud isikud:")
        with open("oiged.txt", "r", encoding="utf-8") as file:
            for line in sorted(file.readlines(), key=lambda x: int(x.split(":")[1]), reverse=True):
                print(line.strip())
    elif valik == "5":
        print("Programm lõpetab töö. Head aega!")
        break
    else:
        print("Vigane valik. Palun valige uuesti.")

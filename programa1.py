while True:
    choice = int(input("1 - nuskaityti, 2 - įrašyti, 0 - išeiti: "))
    if choice == 1:
        try:
            with open("dienorastis.txt", 'r', encoding="UTF-8") as file:
                print(file.read())
        except FileNotFoundError:
            print("Dienoraščio failas dar nesukurtas")
    if choice == 2:
        tekstas = input("Dienoraščio įrašas: ")
        with open("dienorastis.txt", 'a', encoding="UTF-8") as file:
            file.write(tekstas + "\n")
    if choice == 0:
        break
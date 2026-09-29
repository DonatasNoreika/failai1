import pickle

try:
    with open("studentai.pkl", 'rb') as file:
        studentai = pickle.load(file)
except FileNotFoundError:
    studentai = []

while True:
    choice = int(input("1 - nuskaityti, 2 - įrašyti, 0 - išeiti: "))
    match choice:
        case 1:
            for studentas in studentai:
                print(studentas)
        case 2:
            vardas = input("Vardas: ")
            pavarde = input("Pavardė: ")
            kodas = int(input("Kodas: "))
            studentas = {
                "vardas": vardas,
                "pavarde": pavarde,
                'kodas': kodas
            }
            studentai.append(studentas)
            with open('studentai.pkl', 'wb') as file:
                pickle.dump(studentai, file)
        case 0:
            print("Viso gero")
            break
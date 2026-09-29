import pickle

# studentai = [
#     {
#         "vardas": "Jonas",
#         "pavarde": "Jonaitis",
#         "kodas": 45786,
#     },
#     {
#         "vardas": "Petras",
#         "pavarde": "Petraitis",
#         "kodas": 45987,
#     },
# ]
#
# with open('studentai.pkl', 'wb') as file:
#     pickle.dump(studentai, file)

with open("studentai.pkl", 'rb') as file:
    masyvas = pickle.load(file)

print(masyvas[0]['vardas'])
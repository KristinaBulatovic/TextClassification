
# Ucitavanje biblioteka
import cPickle as c
import os
from sklearn import *
from collections import Counter


def load(clf_file):                    # Kreiranje funkcije load kojoj se prosledjuje jedan parametar
    with open(clf_file) as fp:         # Otvaranje fajla ciji naziv se prosledjuje preko parametra clf_file
        clf = c.load(fp)               # Ucitavanje fajla
    return clf                         # Vracanje vrednosti fajla


def make_dict():                       # Kreiranje funkcije make_dict

    # Postavljanje vrednosti parametrima
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    words = []
    c = len(emails)

    for email in emails:                # Petlja koja prolazi kroz svaki email
        f = open(email)                 # Otvaranje email-a
        blob = f.read()                 # Citanje email-a i cuvanje u promenljivoj blob
        words += blob.split(" ")        # Cuvanje svake reci iz promeljive blob kao clanove niza
        print c                         # Ispis na ekran
        c -= 1                          # Smanjivanje promenljive c za jedan


    for i in range(len(words)):         # Prolazak kroz niz reci
        if not words[i].isalpha():      # Provera da li se rec ne sastoji samo od abecednih znakova
            words[i] = ""               # Ukoliko se ne sastoji umesto te reci postavlja prazan string

    dictionary = Counter(words)         # Prebrojavanje clanova niza
    del dictionary[""]                  # Brisanje praznih stringova
    return dictionary.most_common(3000) # Vraca listu najcescih elemenata i koliko puta se ponavljaju


clf = load("text-classifier.mdl")       # Ucitavanje fajla
d = make_dict()                         # Poziv funkcije make_dict


while True:                             # Beskonacna petlja
    features = []                       # Kreiranje niza
    inp = raw_input(">").split()        # Unos sa tastature
    if inp[0] == "exit":                # Proverava da li je rec "exit"
        break                           # Ukoliko jeste izlazi iz petlje
    for word in d:                      # Prolazak kroz listu
        features.append(inp.count(word[0])) # Prebrojavanje reci i njihov unos u niz features
    res = clf.predict([features])       # Testiranje
print ["Not Spam", "Spam!"][res[0]]     # Ispis na ekran
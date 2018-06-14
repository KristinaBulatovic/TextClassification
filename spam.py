"""
pip install sklearn
pip install numpy
pip install scify

python version 2.x.x.
"""


# Ucitavanje biblioteka
import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import cPickle as c


def save(clf, name):                    # Kreiranje funkcije save kojoj se prosledjuju dva parametra
    with open(name, 'wb') as fp:        # Otvaranje ili kreiranje fajla ciji naziv se prosledjuje preko parametra name
        c.dump(clf, fp)                 # Unos podataka u fajl
    print "saved"                       # Ispis na ekran


def make_dict():                        # Kreiranje funkcije make_dict

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


def make_dataset(dictionary):           # Kreiranje funkcije make_dataset kojoj se prosledjuje jedan parametar

    # Postavljanje vrednosti parametrima
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    feature_set = []
    labels = []
    c = len(emails)

    for email in emails:                # Prolazak kroz svaki email
        data = []                       # Kreiranje niza
        f = open(email)                 # Otvaranje email-a
        words = f.read().split(' ')     # Citanje mail-a i cuvanje svake reci kao clanove niza
        for entry in dictionary:        # Prolazak korz listu koja je prosledjena kao parametar
            data.append(words.count(entry[0]))  # Prebrojavanje reci i njihov unos u niz data
        feature_set.append(data)        # Unos liste data u listu feature_set

        if "ham" in email:              # Provera da li je email "ham"
            labels.append(0)            # Ako jeste u listu labels dodaje 0
        if "spam" in email:             # Proverava da li je email "spam"
            labels.append(1)            # Ako jeste u listu labels dodaje 1
        print c                         # Ispis na ekran
        c = c - 1                       # Smanjivanje c za 1
    return feature_set, labels          # Vraca listu feture_set i listu labels


d = make_dict()                         # Pozivanje funkcije make_dict
features, labels = make_dataset(d)      # Pozivanje funkcije make_dataset

x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2) # train_test_split - Postavljanje vrednosti x i y

clf = MultinomialNB()                   # Kreiranje klasifikatora
clf.fit(x_train, y_train)               # Klasifikacija prema x i y

preds = clf.predict(x_test)             # Testiranje
print accuracy_score(y_test, preds)     # Ispis ocene tacnosti klasifikacije na ekran
save(clf, "text-classifier.mdl")        # Pozivanje funkcije save
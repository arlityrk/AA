import csv
import eesti_isikukood
import random

andmed_list = [['SOCIAL_SECURITY_NUMBER', 'FORENAME', 'SURNAME', 'GENDER', 'DATE_OF_BIRTH']]

namefile_content = [line.strip() for line in open('names.txt', 'r', encoding="utf8")]
namefile_content = [item for item in namefile_content if "," in item]

for i in range(0, 1000001):

    tais_nimi = random.choice(namefile_content).split(',')
    eesnimi = tais_nimi[0].strip()
    perenimi = tais_nimi[1].strip()
    # Genereerib kuupäeva kujul yyyymmdd
    synnikuupev = eesti_isikukood.genereeri_synnikuupaev()
    isikukood = eesti_isikukood.isikukood_kp_jargi(synnikuupev)
    # Isikukoodi unikaalsuse kontroll, välja kommenteeritud kuna praegune lahendus võtab liiga palju aega
    """for x in (range(len(andmed_list))):
        while isikukood in andmed_list[x][0]:
            isikukood = eesti_isikukood.isikukood_kp_jargi(synnikuupev)"""

    if isikukood[:1] in ('1', '3', '5', '7'):
        sugu = 'M'
    else:
        sugu = 'F'

    # Viia kuupäev kujule dd.mm.yyyy
    formaaditud_synnikuupaev = synnikuupev[6:8] + "." + synnikuupev[4:6] + "." + synnikuupev[0:4]
    andmed_list.append([isikukood, eesnimi, perenimi, sugu, formaaditud_synnikuupaev])

with open('andmed.csv', 'w+', encoding="utf8") as csvfile:
    # http://stackoverflow.com/questions/1170214/pythons-csv-writer-produces-wrong-line-terminator
    csvwriter = csv.writer(csvfile, delimiter=';', lineterminator='\n')
    csvwriter.writerows(andmed_list)
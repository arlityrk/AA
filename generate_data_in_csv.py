import csv
import eesti_isikukood
import random

namefile_content = [line.strip() for line in open('names.txt', 'r', encoding="utf8")]
namefile_content = [item for item in namefile_content if "," in item]
isikukoodid = eesti_isikukood.gen_n_isikukoodi(1000000)

with open('andmed.csv', 'w+', encoding="utf8") as csvfile:
    # http://stackoverflow.com/questions/1170214/pythons-csv-writer-produces-wrong-line-terminator
    csvwriter = csv.writer(csvfile, delimiter=';', lineterminator='\n')
    csvwriter.writerow(['SOCIAL_SECURITY_NUMBER', 'FORENAME', 'SURNAME', 'GENDER', 'DATE_OF_BIRTH'])
    for i in range(0, 1000000):

        tais_nimi = random.choice(namefile_content).split(',')
        eesnimi = tais_nimi[0].strip()
        perenimi = tais_nimi[1].strip()
        isikukood = isikukoodid[i]

        if isikukood[:1] in ('1', '3', '5', '7'):
            sugu = 'M'
        else:
            sugu = 'F'
        csvwriter.writerow([isikukood, eesnimi, perenimi, sugu,
                            "%d.%d.%d" % (int(isikukood[5:7]), int(isikukood[3:5]), int(isikukood[1:3]))])
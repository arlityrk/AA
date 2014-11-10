import datetime
import random


def genereeri_synnikuupaev():
    """Genereerib suvalise kuupäeva vahemikus 01.01.1800 - sysdate. Tagastab stringina kuupäeva kujul YYYYMMDD"""

    delta = datetime.date.today() - datetime.date(1800, 1, 1)
    synnikuupaev = datetime.date(1800, 1, 1) + datetime.timedelta(random.randint(1, delta.days))
    return synnikuupaev.strftime('%Y%m%d')


def genereeri_poolik_isikukood(synnikuupaev):
    """genereeri_synnikuupaev() funktsiooniga genereeritud suvalisele kuupäevale lisatakse suvaline number vahemikus 000-999.
    Sisendiks võtab kuupäeva formaadis YYYYMMDD. Tagastab stringina isikukoodi 1-10 numbrid"""

    sajand = {'18': ('1', '2'), '19': ('3', '4'), '20': ('5', '6')}
    poolik_isikukood = random.choice(sajand[synnikuupaev[:2]]) + synnikuupaev[2:] + str(random.randint(0, 999)).zfill(3)
    return (poolik_isikukood)


def genereeri_kontrollnr(poolik_isikukood):
    """Genereerib genereeri_poolik_isikukood() funktsiooniga genereritud pooliku isikukoodi põhjal kontrollnumbri isikukoodile.
    Sisendiks võtab stringina isikukoodi esimesed 10 numbrit ning tagastab täieliku isikukoodi stringina"""

    esimese_astme_kaal = "1234567891"
    teise_astme_kaal = "3456789123"
    kontroll_nr = 0

    assert (len(poolik_isikukood) == len(esimese_astme_kaal))
    assert (len(poolik_isikukood) == len(teise_astme_kaal))
    for i in range(10):
        kontroll_nr += int(poolik_isikukood[i]) * int(esimese_astme_kaal[i])
    else:
        if kontroll_nr % 11 != 10:
            return str(kontroll_nr % 11)
        else:
            kontroll_nr = 0
            for j in range(10):
                kontroll_nr += int(poolik_isikukood[j]) * int(teise_astme_kaal[j])
            else:
                if kontroll_nr % 11 != 10:
                    return str(kontroll_nr % 11)
                else:
                    return str(0)


def genereeri_isikukood():
    """Genereerib suvalise isikukoodi isikule kes on sündinud vahemikus 01.01.1800 - sysdate """
    poolik_isikukood = genereeri_poolik_isikukood(genereeri_synnikuupaev())
    return poolik_isikukood + genereeri_kontrollnr(poolik_isikukood)


def isikukood_kp_jargi(synnikuupaev):
    """Genereerib isikukoodi sisendiks antud kuupäeva pealt. Sisendiks võtab kuupäeva formaadis YYYYMMDD"""
    poolik_isikukood = genereeri_poolik_isikukood(synnikuupaev)
    return genereeri_poolik_isikukood(synnikuupaev) + genereeri_kontrollnr(poolik_isikukood)


if __name__ == '__main__':
    print(genereeri_isikukood())









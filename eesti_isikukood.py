import datetime
import random


def gen_synnikuupaev():
    """Genereerib suvalise kuupäeva vahemikus 01.01.1800 - sysdate. Tagastab stringina kuupäeva kujul YYYYMMDD"""

    delta = datetime.date.today() - datetime.date(1800, 1, 1)
    synnikuupaev = datetime.date(1800, 1, 1) + datetime.timedelta(random.randint(1, delta.days))
    return format_synnikp(synnikuupaev)


def gen_sajand(synnikuupaev):
    """Genereerid isikukoodi esimese numbri"""
    sajand = {'18': ('1', '2'), '19': ('3', '4'), '20': ('5', '6')}
    return random.choice(sajand[synnikuupaev[:2]])


def gen_jrknr():
    """Genereerib isikukoodi 8-10 numbrid"""
    return str(random.randint(0, 999)).zfill(3)


def gen_kontrollnr(poolik_isikukood):
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


def format_synnikp(date):
    """Võtab sisendiks date tüüpi kuupäeva ja tagastab selle stringina YYYYMMDD formaadis"""
    return date.strftime('%Y%m%d')


def gen_random_isikukood():
    """Genereerib suvalise isikukoodi isikule kes on sündinud vahemikus 01.01.1800 - sysdate """
    synni_kp = gen_synnikuupaev()
    isikukood = gen_sajand(synni_kp) + synni_kp[2:] + gen_jrknr()
    isikukood += gen_kontrollnr(isikukood)
    return isikukood


def gen_isikukood_kp_ja_jrk_jargi(synnikuupaev, jrk_nr):
    """Genereerib isikukoodi sisendiks antud kuupäeva ja jrk nr pealt. Sisendiks võtab kuupäeva formaadis YYYYMMDD"""
    synni_kp = format_synnikp(synnikuupaev)
    isikukood = gen_sajand(synni_kp) + synni_kp[2:] + str(jrk_nr).zfill(3)
    isikukood += gen_kontrollnr(isikukood)
    return isikukood


def gen_n_isikukoodi(n):
    """Genereerib etteantud arvu unikaalseid isikukoode"""
    valmis = False
    isikukoodid = []
    algne_synnikp = datetime.date(1800, 1, 1)
    for x in range(1, n):
        for y in range(0, 1000):
            isikukoodid.append(gen_isikukood_kp_ja_jrk_jargi(algne_synnikp + datetime.timedelta(x), y))
            if len(isikukoodid) >= n:
                valmis = True
                break
        if valmis:
            break
    return isikukoodid

if __name__ == '__main__':
    print(gen_random_isikukood())










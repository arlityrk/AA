import os
import eesti_isikukood

"""Antud lahendus sõltub platvormist kust koodi jooksutatakse"""

os.system('echo ' + eesti_isikukood.gen_random_isikukood() + '| clip')
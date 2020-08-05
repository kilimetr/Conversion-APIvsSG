# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

import os

os.chdir("/Users/kilimetr/Desktop/python/Conversion-APIvsSG")

from Gravity_fun import SGtoAPI, SGtoBaume

SG = 1.02

API = SGtoAPI(SG)
Baume = SGtoBaume(SG)

print(API)
print(Baume)
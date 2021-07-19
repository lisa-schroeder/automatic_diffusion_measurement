# Add Qmix SDK path to module search path in order to make sure Python finds SDK modules.
import sys
sys.path.append(r"C:/Users/Public/Documents/QmixSDK/lib/python")
from experiment import calcComp, chemicals

# import other modules
import time
import pandas as pd

# create dict chemList including objects of class chemicals
# only necessary, if "Chemicals_database.csv" changed
# chemList = chemicals.getChemicalsList("experiment\\Chemicals_database.csv")           #https://coderslegacy.com/import-class-from-python-file/, https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/

# load chemList
chemList = chemicals.loadChemicalsList("chemList")
# Define mixture
components = ['H2O', 'EtOH']        # enter components as list
# mixratio = [0.9, 0.1]       # enter mixratio as list
print("components: ", components)
amount = 6        # enter total amount of mixture in mL
# vol, M = calcComp.calcComp(chemList, mixratio, components, amount)     # vol is list containing needed volumes of all components
print("volume H2O, EtOH for EtOH 00: ", calcComp.calcComp(chemList, [1, 0], components, amount))
print("volume H2O, EtOH for EtOH 10: ", calcComp.calcComp(chemList, [0.9, 0.1], components, amount))
print("volume H2O, EtOH for EtOH 20: ", calcComp.calcComp(chemList, [0.8, 0.2], components, amount))
print("volume H2O, EtOH for EtOH 30: ", calcComp.calcComp(chemList, [0.7, 0.3], components, amount))
print("volume H2O, EtOH for EtOH 40: ", calcComp.calcComp(chemList, [0.6, 0.4], components, amount))
print("volume H2O, EtOH for EtOH 50: ", calcComp.calcComp(chemList, [0.5, 0.5], components, amount))
print("volume H2O, EtOH for EtOH 60: ", calcComp.calcComp(chemList, [0.4, 0.6], components, amount))
print("volume H2O, EtOH for EtOH 70: ", calcComp.calcComp(chemList, [0.3, 0.7], components, amount))
print("volume H2O, EtOH for EtOH 80: ", calcComp.calcComp(chemList, [0.2, 0.8], components, amount))
print("volume H2O, EtOH for EtOH 90: ", calcComp.calcComp(chemList, [0.1, 0.9], components, amount))
print("volume H2O, EtOH for EtOH 100: ", calcComp.calcComp(chemList, [0, 1], components, amount))


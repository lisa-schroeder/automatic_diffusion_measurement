import pandas as pd
import pickle

# Supporting functions
def SaveToFile(filename, data):
    out_file = open(filename, 'wb')
    pickle.dump(data, out_file)
    out_file.close()

    
class chemical():
    # This class defines chemicals in a way to determine the required volume in order to achieve a certain mixing ratio and to evaluate their compatibility with the ASAB setup.

    def __init__(self, nameShort, nameLong, density, molarMass):
        # Initialize a class object with the specified properties
        self.nameShort = nameShort
        self.nameLong = nameLong
        self.density = density
        self.molarMass = molarMass


def getChemicalsList(dataFile):         #input: .csv-file, output: dict
    # This function loads the .csv database including the information regarding the chemicals and generates objects of the chemicals class. A dictionary containing all the chemicals listed in the database is returned using the NameShort in the database as keys.
    chemInfo = pd.read_csv(dataFile, sep=";")       
    chemList = {}
    for i in chemInfo.index:        #write each chemical as object into the dict
        chem = chemical(chemInfo.loc[i, "NameShort"], chemInfo.loc[i, "NameLong"], chemInfo.loc[i, "Density at 20 degreeC / g/cm3"], chemInfo.loc[i, "Molar mass / g/mol"])
        chemList[chemInfo.loc[i, "NameShort"]] = chem
    # save the chemList dictionary in order to be able to load once it is generated. It does not need to be newly generated, if no changes in the database occured.
    SaveToFile("chemList", chemList)
    return chemList

def loadChemicalsList(file_chemList):   #input: path to pickle file
    # This function loads a saved chemList object.
    load_file = open(file_chemList, 'rb')
    out = pickle.load(load_file)
    load_file.close()
    return out

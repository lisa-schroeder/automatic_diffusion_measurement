# method to calculate the needed volume of each component
def calcComp(chemicals, mixratio, components, amount):
    # chemicals is a dict, key is the name of the chemical, the resulting object has functions .density and .molarMass
    # mixratio is a list, containing the ratio of each component. it doesn't have to add up to one
    # components is a list, containing the names of the chemicals
    # amount is the total amount of solution needed
    # output: vol is a list, containing the volume of each component
    mixratio_norm = []      # create a normalized mixratio list, called mixratio_norm
    for i in range(len(mixratio)):
        mixratio_norm = mixratio_norm + [mixratio[i]/sum(mixratio)]     # https://www.codespeedy.com/how-to-add-all-numbers-in-a-list-in-python/
    M = []      # List including molar masses
    for i in range(len(components)):
        M = M + [chemicals[components[i]].molarMass]   # get the molar mass of each component
    rho = []        # List including densities
    for i in range(len(components)):
        rho = rho + [chemicals[components[i]].density]      # get the density of each component      https://www.w3schools.com/python/python_classes.asp
    volcalc = 0     # Calculate volume fraction-denominator
    for i in range(len(components)):
        volcalc = volcalc + mixratio_norm[i] * M[i] / rho[i]        # volume of one mol liquid * mixratio_norm
    vol = []        # list which will contain volumes of all components
    for i in range(len(components)):
        vol = vol + [mixratio_norm[i] * M[i] / rho[i] / volcalc * amount]       # volume of each component actually needed
    return vol

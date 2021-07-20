# ASAB
This repository contains the modules and files to run the ASAB project.

# pump_binary_mixture.py
This script runs the mixing and measurement process of binary mixtures.
Initializig of pumps and valves is written by Monika Vogler.
Imported libaries need to be installed seperately, these are not part of this GitHub repository.

# experiment
This repository contains:
data of each component as molar mass and density (chemicals.py and Chemicals_database.csv);
database of chemicals is converted to a pickle file(chemicals.py), written by Monika Vogler;
calculation how much volume of which component is needed (calcComp.py)

# evaluation
This repository contains:
script to calculate the self-diffusion coefficient from integral values (evaluation_diffusion_py);
integrals of measured data (integral_values_manual.csv, integral_values_automated.csv);
calculated self-diffusion coefficient (diffusion_coefficient_manual.csv, diffusion_coefficient_automated.csv)
coefficient of determination R^2 (diffusion_coefficient_r_sq_manual.csv, diffusion_coefficient_r_sq_automated.csv)

# tests
This repository contains the test of the calculation script (testCalcComp.py)

# test_pump_accuracy.py
Script which was used to determine the accuracy of the syringes

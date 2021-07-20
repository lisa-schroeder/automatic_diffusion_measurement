# https://realpython.com/linear-regression-in-python/

import numpy as np
from numpy import log as ln     # https://www.delftstack.com/howto/numpy/natural-log-python/
from sklearn.linear_model import LinearRegression
import math
import pandas as pd

# used parameters
gyromagn_ratio = 2.675*10**8        # rad*T^(-1)*s^(-1)
gradient_length = 0.004     # sec, D71
diffusion_time = 0.025      # sec, D74
maximum_gradient = 0.2977       # T*m^(-1)
relative_gradient = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

# import values to evaluate
values = pd.read_csv("integral_values_automated.csv", sep=",", header = None)
print(values)


def find_D(values):
    # calculate the values of the x-axis
    x = np.array([None]*len(relative_gradient))
    for i in range(10):
        # Stejskal-Tanner plot: x-axis
        x[i] = 2*(gyromagn_ratio**2)*((gradient_length*(2/math.pi))**2)*((maximum_gradient*relative_gradient[i])**2)*(diffusion_time/2-(gradient_length*(2/math.pi))/3)*(10**(-9))
    x = x.reshape((-1, 1))

    D = []      # list in which diffusion coefficients will be entered

    for i in range(len(values.columns)):
        # y_raw is list containing integrals as values
        y_raw = []
        # calculate the values of the y-axis
        for j in range(len(relative_gradient)+1):
            y_raw = y_raw + [float(values.loc[j+1, i])]

        # y is list containing ln(I/I_0) as values for Stejskal-Tanner plot: y-axis
        y = []
        for j in range(len(y_raw)-1):
            y = y + [ln(y_raw[j+1]/y_raw[0])]

       # do a linear regression
        model = LinearRegression().fit(x, y)        # https://realpython.com/linear-regression-in-python/

        D = D + [[values.loc[0, i], -model.coef_[0]]]

    return(D)

# export results in .csv file
D = find_D(values)
data_frame = pd.DataFrame(D)
data_frame.columns = ['Measurement', 'Diffusion Coefficient in 10^(-9) m^2 s^(-1)']
data_frame.to_csv("diffusion_coefficient_automated.csv")

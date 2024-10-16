import matplotlib.pyplot as plt

import numpy as np 
import plottools
from plottools import set_colorbar_max_min_values

x = np.linspace(0, 10, 101)
y = np.linspace(0, 10, 101)
xg, yg = np.meshgrid(x, y)
zg = np.sin(xg + yg)  
zg1 = 1e8 *zg + 3e8
zg2 = 1.123213 * zg
zg3 = zg2 + 213987

def make_plot(zg):
    plt.figure()
    plt.pcolor(xg, yg, zg)
    cbar = plt.colorbar()
    set_colorbar_max_min_values(cbar)
    

make_plot(zg)
make_plot(zg1)
make_plot(zg2)
make_plot(zg3)
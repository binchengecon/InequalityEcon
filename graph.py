import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
import csv
import pandas as pd



gamma = 0.5
r = 0.03
rho = 0.05
Var = 0.07
Corr = 0.9
the = -np.log(Corr)
sig2 = 2*the*Var
zmean = np.exp(Var/2)

# Solution parameters (domain on which to solve PDE)
X_low = np.array([-0.02, zmean*0.8])  # wealth lower bound
X_high = np.array([4, zmean*1.2])          # wealth upper bound

n_plot = 600  # Points on plot grid for each dimension


aspace = np.linspace(-0.02, 4, n_plot)
zspace = np.linspace(zmean*0.8, zmean*1.2, n_plot)
A, Z = np.meshgrid(aspace, zspace)

Moll_Vacenter = pd.read_csv("./MollData/Va_center.csv", header = None)

fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A, Z, Moll_Vacenter, cmap='viridis')
ax.view_init(35, 35)
ax.set_xlabel('$a$')
ax.set_ylabel('$z$')
ax.set_zlim(0.75,1.10)
# ax.set_zlabel('$\partial V / \partial a$')
# ax.set_zlabel('Difference')
# ax.set_title('Deep Learning Solution')
plt.savefig('./MollData/Va_center_py.png',bbox_inches='tight')


Moll_Va = pd.read_csv("./MollData/Va_Upwind.csv", header = None)

fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A, Z, Moll_Va, cmap='viridis')
ax.view_init(35, 35)
ax.set_xlabel('$a$')
ax.set_ylabel('$z$')
ax.set_zlim(0.75,1.10)
# ax.set_zlabel('$\partial V / \partial a$')
# ax.set_zlabel('Difference')
# ax.set_title('Deep Learning Solution')
plt.savefig('./MollData/VaUpwind_py.png',bbox_inches='tight')

Moll_Vaa_center = pd.read_csv("./MollData/Vaa_center.csv", header = None)

fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A, Z, Moll_Vaa_center, cmap='viridis')
ax.view_init(35, 35)
ax.set_xlabel('$a$')
ax.set_ylabel('$z$')
# ax.set_zlim(0.75,1.10)
# ax.set_zlabel('$\partial V / \partial a$')
# ax.set_zlabel('Difference')
# ax.set_title('Deep Learning Solution')
plt.savefig('./MollData/Vaa_center_py.png',bbox_inches='tight')


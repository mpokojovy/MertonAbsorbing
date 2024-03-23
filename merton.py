# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:40:29 2024

@author: Yaacov Kopeliovich and Michael Pokojovy
"""

import os
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True

os.chdir("???")

kappa = 1.5; # (mu - r)/sigma^2

PI = lambda kappa, gamma: 0.5*((kappa + 1) - np.sqrt((1 - kappa)*(1 - kappa) + 4*gamma))

kappa = np.linspace(-2.0, 4.0, num = 500)

plt.plot(kappa, kappa, 'k-')
plt.xlabel(r'$(r - \mu)/\sigma^2$')
plt.ylabel(r'Pre-bankruptcy Merton ratio')

plt.plot(kappa, PI(kappa, 0.01), 'r--')
plt.plot(kappa, PI(kappa, 0.1), 'g-.')
plt.plot(kappa, PI(kappa, 1.0), 'b:')

plt.legend([r'$\lambda = 0$ (classic)', r'$\lambda = 0.01 \, \sigma^2$', 
            r'$\lambda = 0.1 \, \sigma^2$', r'$\lambda = 1.0 \,\sigma^2$'])

plt.savefig('Merton-ratio.pdf', format = 'pdf', bbox_inches = 'tight')
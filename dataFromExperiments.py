#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import subprocess
import pickle
import numpy as np
from matplotlib import cm
import scipy.stats
from scipy.optimize import curve_fit

Kanavarioti2001 = [6.6, 25.8, 18.4, 13.1, 10.4, 9.5, 7.0, 4.5, 2.8, 1.1, 0.3,0.0]
Ding1996 = [72, 21, 2.6, 0.6, 0.2, 0.1,0.0]
Ferris1999 = [30, 42, 12, 6.2, 3.3, 1.8, 1.0,0.0]

distr1 = np.array([item/sum(Kanavarioti2001) for item in Kanavarioti2001])
distr2 = np.array([item/sum(Ding1996) for item in Ding1996])
distr3 = np.array([item/sum(Ferris1999) for item in Ferris1999])
x1 = np.array(list(range(1,len(distr1)+1)))
x2 = np.array(list(range(1,len(distr2)+1)))
x3 = np.array(list(range(1,len(distr3)+1)))
xg = np.array(list(range(1,16)))

def func(l,a):
    return a**2*l*(1-a)**(l-1)
popt1, pcov1 = curve_fit(func, x1[1:], distr1[1:])
y1= func(xg,popt1[0])
popt2, pcov2 = curve_fit(func, x2, distr2)
y2= func(xg,popt2[0])
popt3, pcov3 = curve_fit(func, x3, distr3)
y3= func(xg,popt3[0])

plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
fig = plt.figure(1, figsize=(9,6))
ax = fig.add_subplot(111)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

ax.plot(xg,y1,linewidth=6,c='r',alpha=0.75)
ax.plot(xg,y2,linewidth=6,c='magenta',alpha=0.75)
ax.plot(xg,y3,linewidth=6,c='cyan',alpha=0.75)
ax.scatter(x1[:-1],distr1[:-1],marker='o',s=150,c='r')

ax.scatter(x2[:-1],distr2[:-1],marker='v',s=150,c='magenta')
ax.scatter(x3[:-1],distr3[:-1],marker='d',s=150,c='cyan')
ax.set_yscale('log')
ax.set_xticks([1,5,10,15])
ax.set_xticklabels([r"$\mathbf{1}$",r"$\mathbf{5}$",
                    r"$\mathbf{10}$",r"$\mathbf{15}$"],fontsize=25)
ax.set_yticks([0.0001,0.01,1])
ax.set_yticklabels(
    [r"$\mathbf{10^{-4}}$",r"$\mathbf{10^{-2}}$",r"$\mathbf{1}$"],
    fontsize = 25)
ax.get_yaxis().get_major_formatter().labelOnlyBase = False
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5)
ax.set_ylabel('ratio of chains',fontsize = 30)
ax.set_xlabel('length',fontsize = 30)
ax.set_xlim(0,15)
ax.set_ylim(0.0001,1)
plt.show()



# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 10:56:25 2025

@author: nacho
"""

import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from scipy.special import eval_hermite
from scipy.special import factorial

#4.1
def eq41(y, t):
# y[0] omega (theta prima)
# y[1] theta
# return omegaprima, thetaprima
    return -g/L*np.sin(y[1])+(-b*y[0]+A*np.cos(Omega*t))/(m*L**2) , y[0]
#Defineixo la ecuació diferencial

g = 1
L = 1
Omega = 0.666
b = 0.5
m = 1
A = 1.35
#Variables

t = np.linspace(1, 100, 10000)
ci = [0, 0.01*np.pi]
res = spi.odeint(eq41, ci, t)
#Soluciono la equdif

plt.figure()
plt.suptitle("Pèndol esmorteït i forçat")
plt.plot(t, res[:, 0], label = "Omega")
plt.plot(t, res[:, 1], label = "Theta")
plt.grid(True)
plt.legend(loc="lower left")
#Grafico

#4.2
def eq42(psi, x):
# psi[0] = psi
# psi[1] = psiprima
    return psi[1], -B*((2*n+1)-B*x**2)*psi[0]
#Defineixo la ecuació diferencial

B = 1
x = np.linspace(-5, 5, 1000)
x1 = np.linspace(0, 5, 500)
x2 = np.linspace(0, -5, 500)
ci = np.array([[0.751126, 0.], [-0.531125, 0.], [0.459969, 0.]])
#Separo x en dos arrays, un creixent i un decreixent. Creo un array d'arrays indexats que recorrerà un bucle

plt.figure(figsize=(6, 12))
plt.suptitle("Oscil·lador harmònic quàntic")

for n in range (0, 5, 2):
    H =  eval_hermite(n, x)
    funcionsHerm = (2**n*factorial(n)*(np.pi)**(1/2))**(-1/2)*np.exp(-x**2/2)*H
    plt.subplot(211)
    plt.title("Funcions d'Hermite")
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("Hn")
    plt.plot(x, funcionsHerm, label = f"n={n}")
    plt.legend(loc="lower left")
    plt.ylim(-0.6, 0.8)
    plt.xlim(-5, 5)
    #Grafico les funcions d'Hermite
    
    cin = ci[n//2]
    #Faig servir les c.i. indexades
    res1 = spi.odeint(eq42, cin, x1)
    res2 = spi.odeint(eq42, cin, x2)
    #Resolc les equacions diferencials per x<0 i x>0 per separat
    res2inv = res2[::-1, :]
    #Inverteixo la solució negativa per que vagi de -5 a 0
    res = np.vstack((res2inv, res1))
    #Ajunto els dos arrays de la solució
    plt.subplot(212)
    plt.title("Equació diferencial")
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel(r"$\Psi$")
    plt.plot(x, res[:, 0], label = f"n={n}")
    plt.legend(loc="lower left")
    plt.ylim(-0.6, 0.8)
    plt.xlim(-5, 5)
    #Grafico

#4.3
def eq43(x, t):
# x[0] = x1
# x[1] = v1
# x[2] = x2
# x[3] = v2
    return x[1], (k2*x[2]-(k1+k2)*x[0])/m, x[3], (k2*x[0]-(k1+k2)*x[2])/m
#Defineixo les ecuacions diferencials

m = 1
k1 = 10
k2 = 0.5
#Variables 

ci = [1, 0, 0, 0]
t = np.linspace(0, 40, 1000)
res = spi.odeint(eq43, ci, t)
#Soluciono la ecuació

plt.figure(figsize=(6, 12))
plt.suptitle("Oscil·ladors acoblats")
plt.tight_layout()
plt.subplot(211)
plt.title("x(t)")
plt.xlabel("Temps (s)")
plt.ylabel("Posició objecte")
plt.grid(True)
plt.plot(t, res[:, 0], label = r"$x_1$")
plt.plot(t, res[:, 2], label = r"$x_2$")
plt.legend(loc="lower left")
#Gràfic de la posició

plt.subplot(212)
plt.title("v(t)")
plt.xlabel("Temps (s)")
plt.ylabel("Velocitat objecte")
plt.grid(True)
plt.plot(t, res[:, 1], label = r"$v_1$")
plt.plot(t, res[:, 3], label = r"$v_2$")
plt.legend(loc="lower left")
#Gràfic de la velocitat

#4.4
def eq44(x, t):
# x[0] = x
# x[1] = vx
# x[2] = y
# x[3] = vy
    return x[1], -(G*M*x[0])/((x[0]**2 + x[2]**2)**(3/2)), x[3], -(G*M*x[2])/((x[0]**2 + x[2]**2)**(3/2)) 
#Defineixo les equacions diferencials

G = 6.67e-11 
M = 1.9891e30 
au = 1.49598e11 
#Dades generals

aphelionH = 35.082 * au
velapH = 0.869e3 
TH = 3.15576e7 * 75.32
#Dades Halley

aphelionT = 1.0167 * au
velapT = 29260
TT = 365.2564 * 24 * 60 * 60
#Dades Terra

ciH = (aphelionH, 0, 0, velapH)
tH = np.linspace(0, TH, 10000)
solH = spi.odeint(eq44, ciH, tH)
vH = np.sqrt(solH[:, 1] **2 + solH[:, 3] **2)
#Solucins Halley

ciT = (aphelionT, 0, 0, velapT)
tT = np.linspace(0, TT, 10000)
solT = spi.odeint(eq44, ciT, tT)
vT = np.sqrt(solT[:, 1] **2 + solT[:, 3] **2)
#Solucins Terra

plt.figure(figsize=(8, 8))
plt.suptitle("Halley")
plt.subplot(221)
plt.title("x(t)")
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.grid(True)
plt.plot(tH, solH[:, 0])
plt.subplot(222)
plt.title("y(t)")
plt.xlabel("t(s)")
plt.ylabel("y(m)")
plt.grid(True)
plt.plot(tH, solH[:, 2])
plt.subplot(223)
plt.title("|v|(t)")
plt.xlabel("t(s)")
plt.ylabel("|v|(m/s)")
plt.grid(True)
plt.plot(tH, vH)
plt.subplot(224)
plt.title("y(x)")
plt.xlabel("x(m)")
plt.ylabel("y(m)")
plt.grid(True)
plt.plot(solH[:, 0], solH[:, 2], label = "Halley")
plt.plot(solT[:, 0], solT[:, 2], label = "Terra")
plt.legend(loc="upper left")
plt.xlim(-2e11, 5.3e12)
plt.ylim(-2.75e12, 2.75e12)
plt.tight_layout()
#Gràfics Halley

plt.figure(figsize=(8, 8))
plt.suptitle("Terra")
plt.subplot(221)
plt.title("x(t)")
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.grid(True)
plt.plot(tT, solT[:, 0])
plt.subplot(222)
plt.title("y(t)")
plt.xlabel("t(s)")
plt.ylabel("y(m)")
plt.grid(True)
plt.plot(tT, solT[:, 2])
plt.subplot(223)
plt.title("|v|(t)")
plt.xlabel("t(s)")
plt.ylabel("|v|(m/s)")
plt.grid(True)
plt.plot(tH, vT)
plt.subplot(224)
plt.title("y(x)")
plt.xlabel("x(m)")
plt.ylabel("y(m)")
plt.grid(True)
plt.plot(solT[:, 0], solT[:, 2])
plt.xlim(-1.6e11, 1.6e11)
plt.ylim(-1.6e11, 1.6e11)
plt.tight_layout()
#Gràfics Terra

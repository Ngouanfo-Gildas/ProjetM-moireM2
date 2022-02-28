import math
import csv
import numpy as np
import pandas as pd

""" Gaussian Dispersion Modeling """

f = lambda g, Ta, Ts, V : (g/np.pi)*V*((Ts-Ta)/Ts)

delta_h = lambda F, u, x : 1.6*(F**(1/3))*(x**(2/3))/u

sigma_y = lambda x, ay, by : ay*np.abs(x)**by

sigma_z = lambda x, az, bz : az*np.abs(x)**bz

def gaussianDM(x, y, z, u, V, Q, hs, g, ay, az, by, bz, Ta, Ts):
    """ Concentration du polluant au point (0, 0, hs) """
    F = f(g, Ta, Ts, V)
    Delta_h = delta_h(F, u, x)
    H = hs + Delta_h
    z = hs
    sigmaY = sigma_y(x, ay, by)
    sigmaZ = sigma_z(x, az, bz)
    c = Q/(2.*np.pi*u*sigmaY*sigmaZ) * np.exp(-y**2/(2.*sigmaY**2))\
        * (np.exp(-(z-H)**2/(2*sigmaY)) + np.exp(-(z+H)**2./(2.*sigmaY)))
    return  c

def read_data(data_file):
    with open(data_file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        list_of_csv = list(csv_reader)
    return list_of_csv

# Calcul des Zi
def pollutionZone(P, I, C0):
    M = len(I)
    N = len(P)
    W = np.zeros((M,N), dtype=int)
    Z = np.zeros((M,N), dtype=list)
    # paramètres
    C0 = 0.034
    Q = 1.59
    hs = 25
    u = 5
    Ts = 30
    Ta = 25
    g = 9.8
    ay = 0.34
    by = 0.82
    az = 0.275
    bz = 0.69
    V = 0.603
    for i in range(M):
        for p in range(N):
            x = p.x
            y = p.y
            z = 0
            X = gaussianDM(x, y, z, u, V, Q, hs, g, ay, az, by, bz, Ta, Ts)
            if X >= C0:
                W[i][p] = 1
                Z[i].append(P[p])
    return W


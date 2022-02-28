from GDModeling.py import *

I = read_data_pd("pollution_source_positions.csv")
P = read_data_pd("potentials_positions.csv")
C0 = 0.034
pollutionZone(P, I, C0)
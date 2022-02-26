
import random
import math
import matplotlib.pyplot as plt
import numpy as np
import csv

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

    def distance(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def point_aleatoire(self, longu: int, larg: int):
        self.x = random.randint(0, longu)
        self.y = random.randint(0, larg)
        return self


"""def show_genome(rayonC, rayonS, genome: Individu, events: list):
    alpha = np.linspace(0, 2*np.pi, 200)
    for event in events:
        xs = event.x
        ys = event.y
        plt.plot(xs, ys, "s", color="black")

    for node in genome:
        cx = node.x
        cy = node.y

        xc = cx + rayonC*np.cos(alpha)
        yc = cy + rayonC*np.sin(alpha)

        xs = cx + rayonS*np.cos(alpha)
        ys = cy + rayonS*np.sin(alpha)

        plt.plot(cx, cy, "o", color="red")
        plt.plot(xc, yc, "b")
        plt.plot(xs, ys, "g")
    
    plt.grid(linestyle='-')
    plt.axis("equal")
    plt.show()"""

# Générer les positions potentielles (des points)
def generate_potentials_positions(longu: int, larg: int, distance: int):
    """ long = longueur de la zone d'intérêt,\n
        larg = largeur de la zone d'intérêt,\n
        distance = paramètre de discrétisation. """
    data_file = "./potentials_positions.csv"
    header = ["abs", "ord"]
    # potentials_positions = []
    with open(data_file,"w", newline="") as csv_file:
        write = csv.writer(csv_file, delimiter=",")
        write.writerow(header)
        i = distance
        while i < longu:
            j = distance
            while j < larg:
                # potentials_positions.append(Point(i, j))
                xp = i
                yp = j
                write.writerow([xp, yp])
                j += distance
            i += distance
    # return potentials_positions

# Générer des sources de pollution aléatoires
def generate_src_pollutions(longu: int, larg: int, nb_of_src: int):
    """ nb_of_src: nombre de sources de pollution à générer, \n
        long = longueur de la zone d'intérêt,\n
        larg = largeur de la zone d'intérêt.""" 
    data_file = "./pollution_source_positions.csv"
    header = ["abs", "ord"]
    source_pollution = [Point() for i in range(nb_of_src)]
    with open(data_file,"w", newline="") as csv_file:
        write = csv.writer(csv_file, delimiter=",")
        write.writerow(header)
        for i in range(nb_of_src):
            source_pollution[i] = source_pollution[i].point_aleatoire(longu, larg)
            xp = source_pollution[i].x
            yp = source_pollution[i].y
            write.writerow([xp, yp])
    # return source_pollution

# Afficher les sources de pollutions
def show_positions(positions: list, couleur: str):
    for event in positions:
        xs = event.x
        ys = event.y
        plt.plot(xs, ys, "s", color=couleur)
    plt.axis("equal")
    plt.show()

# Afficher les positions potentielles et les positions sources de pollution
def show_pos_src(potentials_positions: list, source_pollution: list):
    for src in source_pollution:
        xs = src.x
        ys = src.y
        plt.plot(xs, ys, "o", color="red")

    for ppos in potentials_positions:
        cx = ppos.x
        cy = ppos.y
        plt.plot(cx, cy, "o", color="black")
    
    plt.grid(linestyle='-')
    plt.axis("equal")
    plt.show()

generate_potentials_positions(1000, 1000, 50)
generate_src_pollutions(1000, 1000, 15)


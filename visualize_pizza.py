import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import ListedColormap


file_names = ['small']#, 'medium', 'big']

def load_pizza_data(name):
    data = np.loadtxt(name, dtype=np.str, skiprows=1)
    pizza = np.zeros((len(data),len(data[0])), dtype=np.int)
    for i in range(len(data)):
        pizza[i] = [0 if c == 'T' else 1 for c in data[i]]
    return pizza

def visualize_pizza(name):
    pizza = load_pizza_data(name+'.in')
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')
    ax1.matshow(pizza)
    plt.show()
    
def load_solution_data(name):
    # assumes >1 solutions
    return np.loadtxt(name,dtype=np.int, skiprows=1) 

def visualize_solution(name):
    pizza = load_pizza_data(name+'.in')
    solutions = load_solution_data(name+'.out')
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')

    # visualize pizza
    cmap = ListedColormap(['w', 'y'])
    ax1.matshow(pizza, cmap=cmap)

    for i in range(solutions.shape[0]):
        left_upper_corner_y = solutions[i,0]-0.5
        left_upper_corner_x = solutions[i,1]-0.5
        right_lower_corner_y = solutions[i,2]-solutions[i,0]+1.0
        right_lower_corner_x = solutions[i,3]-solutions[i,1]+1.0

        ax1.add_patch(
            patches.Rectangle(
                (left_upper_corner_x, left_upper_corner_y),   # (x,y)
                right_lower_corner_x,          # width
                right_lower_corner_y,          # height
                fill=False,
                hatch='\\'
            )
        )
    plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import my_function


def plot_function_3d(function_name):
    fig = plt.figure(figsize=(5,5), dpi=200)
    ax = plt.axes(projection='3d')

    x = np.linspace(my_function.min_val - 1, my_function.max_val + 1, 100)
    y = np.linspace(my_function.min_val - 1, my_function.max_val + 1, 100)

    X, Y = np.meshgrid(x, y)
    z = my_function.my_function(X, Y)

    #ax.contour3D(X, Y, z, 200)
    ax.plot_surface(X, Y, z, cmap="plasma", lw=0.5, rstride=1, cstride=1)
    ax.contour(X, Y, z, 10, lw=3, cmap="Pastel2", linestyles="solid", offset=0)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.view_init(45, 45)

    plt.savefig(function_name + '/' + function_name + '3D.png')


def plot_graph(particles, title, color, global_postion):
    fig = plt.figure(figsize=(5,5), dpi=200)
    ax = plt.axes()

    x = np.linspace(my_function.min_val - 1, my_function.max_val + 1, 100)
    y = np.linspace(my_function.min_val - 1, my_function.max_val + 1, 100)

    X, Y = np.meshgrid(x, y)
    z = my_function.my_function(X, Y)

    if color == 'Pastel1':
        for particle in particles:
            if my_function.min_val < particle.position[0] < my_function.max_val and my_function.min_val < particle.position[1] < my_function.max_val:
                ax.scatter(particle.position[0], particle.position[1], c='#32CAF6', zorder=20)

        ax.scatter(global_postion[0], global_postion[1], c='r', zorder=21)

    ax.contour(x, y, z, cmap= color)
    plt.title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.savefig(my_function.function_name + '/' + title + '.png')

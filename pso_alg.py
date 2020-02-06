from plot import plot_graph
import numpy as np
import my_function
from particle import Swarm
from particle import Particle

max_iteration = 100
max_particle = 50
to_plot = False


def init(max_it, pop_size, plot_allowed):
    global max_iteration, max_particle, to_plot
    max_iteration = max_it
    max_particle = pop_size
    to_plot = plot_allowed


def w(iteration):  # Values 0.9 -> 0.4
    return -0.5 * iteration / max_iteration + 0.9


def cp(iteration):  # Values 2.5 -> 0.5
    return -2 * iteration / max_iteration + 2.5


def cg(iteration):  # Values 0.5 -> 2.5
    return 2 * iteration / max_iteration + 0.5


def pso():
    swarm = Swarm()
    particle0 = Particle(my_function.min_val, my_function.max_val)
    swarm.particles.append(particle0)
    swarm.global_best_position = particle0.position
    particle0.best_value = my_function.my_function(particle0.position[0], particle0.position[1])
    swarm.global_best_value = particle0.best_value

    for i in range(0, max_particle - 1):
        particle = Particle(my_function.min_val, my_function.max_val)
        swarm.particles.append(particle)
        value = my_function.my_function(particle.position[0], particle.position[1])
        particle.best_value = value
        if value < swarm.global_best_value:
            swarm.global_best_value = value
            swarm.global_best_position = particle.position

    if to_plot:
        plot_graph(None, my_function.function_name, 'viridis', None)
        plot_graph(swarm.particles, 'initial state', 'Pastel1', swarm.global_best_position)

    # position(k+1) = position(k) + v(k+1)
    # v(k+1) = w(k+1) * v(k) +
    #           cp(k+1) * rand * (best_position(k) - position(k)) +
    #           cg(k+1) * rand * (global_best_position - position(k))
    for it in range(0, max_iteration):
        for particle in swarm.particles:
            v_kplus1 = w(it) * particle.prev_v + \
                       cp(it) * np.random.random() * (particle.best_position - particle.position) + \
                       cg(it) * np.random.random() * (swarm.global_best_position - particle.position)
            next_position = particle.position + v_kplus1
            value = my_function.my_function(particle.position[0], particle.position[1])
            if value < particle.best_value:
                particle.best_value = value
                particle.best_position = next_position
            particle.position = next_position
            particle.prev_v = v_kplus1

        for particle in swarm.particles:
            value = my_function.my_function(particle.position[0], particle.position[1])

            if value < swarm.global_best_value:
                swarm.global_best_value = value
                swarm.global_best_position = particle.position

        if it % (max_iteration // 10) == 0 and to_plot:
            plot_graph(swarm.particles, 'iteration ' + str(it + 1), 'Pastel1', swarm.global_best_position)

    if to_plot:
        plot_graph(swarm.particles, 'final state', 'Pastel1', swarm.global_best_position)

    print('x = {0}'.format(swarm.global_best_position[0]))
    print('y = {0}'.format(swarm.global_best_position[1]))
    print('Global best = {0}'.format(swarm.global_best_value))

    analytic_xy, analytic_best = my_function.analytic_result()
    print('\nPontos eredmény:')
    print('x = {0}'.format(analytic_xy[0]))
    print('y = {0}'.format(analytic_xy[1]))
    print('Global best = {0}'.format(analytic_best))

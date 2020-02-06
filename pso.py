import sys, getopt, pathlib, glob, os, my_function, pso_alg
from plot import plot_function_3d

iteration = 100
population = 50
function = 'sphere'
to_plot = False
plot_num = 10
functions = ['rastrigin', 'ackley', 'sphere', 'rosenbrock', 'easom', 'griewank', 'styblinski']


def initialize():
    global to_plot


    my_function.init(function)
    pso_alg.init(iteration, population, to_plot)

    if to_plot:
        pathlib.Path(function).mkdir(exist_ok=True)
        files = glob.glob(function + '/*')
        for f in files:
            os.remove(f)

        plot_function_3d(function)


if __name__ == '__main__':
    arguments = sys.argv[1:]

    try:
        opts, args = getopt.getopt(arguments, "hp", ["iteration=", "population=", "function="])
    except getopt.GetoptError:
        print('Type: \'pso.py -h\' for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Lehetséges flag-ek:')
            print('-h Segítség')
            print('--iteration 100 - maximális ciklusszám')
            print('--population 50 - egyedek száma')
            print('--function rastrigin - tesztfüggvény')
            print('-p Grafikus ábrázolás\n')
            print('Lehetséges tesztfüggvények:')
            print('rastrigin függvény')
            print('ackley függvény')
            print('sphere függvény')
            print('rosenbrock függvény')
            print('easom függvény')
            print('griewank függvény')
            print('styblinski függvény')
            sys.exit()
        elif opt == '--iteration':
            try:
                iteration = int(arg)
                if iteration < 10:
                    print('Ciklusszám legalább 10 kell hogy legyen')
                    sys.exit(2)
            except ValueError:
                print('Ciklusszám csak pozitív egész szám lehet (10-töl nagyobb)')
                sys.exit(2)
        elif opt == '--population':
            try:
                population = int(arg)
                if population <= 0:
                    print('Az egyedek száma csak pozitív egész szám lehet')
                    sys.exit(2)
            except ValueError:
                print('Az egyedek száma csak pozitív egész szám lehet')
                sys.exit(2)
        elif opt == '--function':
            if arg.lower() in functions:
                function = arg.lower()
            else:
                print('A \'{0}\' függvény ismeretlen\nSegítségért írd be: python pso.py -h'.format(arg))
                sys.exit(2)
        elif opt == '-p':
            to_plot = True

    initialize()
    # pso_alg.pso()

# Részecske-raj optimalizáció (PSO)

```
python pso.py
```

## Command line arguments

`-h` - súgó

`--iteration` - ciklusszám

`--population` - részecskék száma

`--function` - függvény neve a lehetséges függvények közül

`-p` - grafikus megjelenítés: 10 képet nyomtat a folyamatról a kiválasztott függvény nevű mappába

## Választható függvények

### Ackley függvény `ackley`

Globális optimum: `f(0, 0) = 0`

![ackley](functions/ackley3D.png)

### Easom függvény `easom`

Globális optimum: `f(pi, pi) = -1`

![easom](functions/easom3D.png)

### Griewank függvény `griewank`

Globális optimum: `f(0, 0) = 0`

![griewank](functions/griewank3D.png)

### Rastrigin függvény `rastrigin`

Globális optimum: `f(0, 0) = 0`

![rastrigin](functions/rastrigin3D.png)

### Rosenbrock függvény `rosenbrock`

Globális optimum: `f(1, 1) = 0`

![rosenbrock](functions/rosenbrock3D.png)

### Szférikus függvény `sphere`

Globális optimum: `f(0, 0) = 0`

![sphere](functions/sphere3D.png)

### Styblinksi függvény `styblinski`

Globális optimum: `f(-2.903534, -2.903534) = -78.332`

![styblinski](functions/styblinski3D.png)

## Követelmények

Python 3.8

NumPy

matplotlib

OS: Linux

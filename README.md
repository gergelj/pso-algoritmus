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

![](functions/ackley3d.png)

Globális optimum: `f(0, 0) = 0`

### Easom függvény `easom`

![](functions/easom3d.png)

Globális optimum: `f(pi, pi) = -1`

### Griewank függvény `griewank`

![](functions/griewank3d.png)

Globális optimum: `f(0, 0) = 0`

### Rastrigin függvény `rastrigin`

![](functions/rastrigin3d.png)

Globális optimum: `f(0, 0) = 0`

### Rosenbrock függvény `rosenbrock`

![](functions/rosenbrock3d.png)

Globális optimum: `f(1, 1) = 0`

### Szférikus függvény `sphere`

![](functions/sphere3d.png)

Globális optimum: `f(0, 0) = 0`

### Styblinksi függvény `styblinski`

![](functions/styblinski3d.png)

Globális optimum: `f(-2.903534, -2.903534) = -78.332`

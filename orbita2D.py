import math
G = 6.674 * 10 ** (-11)
Mt = 5.972 * 10 ** 24
Rt = 6.371 * 10 ** 6
def calcular_aceleracao(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    a = (G * Mt) / r ** 2
    ax = ((-1) * a * x) / r
    ay = ((-1) * a * y) / r
    return ax, ay
x_sat = Rt + 400000
y_sat = 0
ax, ay = calcular_aceleracao(x_sat, y_sat)
print(ax, ay)

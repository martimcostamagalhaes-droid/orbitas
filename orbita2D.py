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
xsat = Rt + 400000
ysat = 0
vx = 0
vy = 7672
dt = 1           
tempo_total = 100
tempo_atual = 0
while tempo_atual < tempo_total:
    ax, ay = calcular_aceleracao(xsat, ysat)
    vx = vx + ax * dt
    vy = vy + ay * dt
    xsat = xsat + vx * dt
    ysat = ysat + vy * dt
    tempo_atual = tempo_atual + dt
    print("posicao final X:", xsat, "Y:", ysat)
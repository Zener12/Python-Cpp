# Суть: Рассчитайте, когда логотип DVD впервые попадет в любой угол,
# если логотип всегда появляется в левом нижнем углу (старт)

def dvd_logo_position(n, m):
    x, y = 0, 0
    dx, dy = 1, 1
    while True:
        if x + dx == n or x + dx == -1:
            dx = -dx
        if y + dy == n or y + dy == -1:
            dy = -dy
        x += dx
        y += dy
        if (x, y) in ((0,0), (0,m), (n,0), (n,m)):
            return (x, y)

a = list(map(int, input().split()))
n, m = a[0], a[1]
if dvd_logo_position(n, m) == (0, 0):
    print('Левая нижняя часть экрана')
elif dvd_logo_position(n, m) == (0, m):
    print('Правая нижняя часть экрана')
elif dvd_logo_position(n, m) == (n, 0):
    print('Левая верхняя часть экрана')
elif dvd_logo_position(n, m) == (n, m):
    print('Правая верхняя часть экрана')
else:
    print(0)
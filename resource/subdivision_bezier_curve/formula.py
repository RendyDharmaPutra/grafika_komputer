# Subdivision Formula
def div(n: int, m: int, x: int, y: int) :
    return ((y - x) * n + x * m) / y

def subdiv(n: tuple[int, int], m: tuple[int, int], x: int, y: int) :
    coorX = div(n[0], m[0], x, y)
    coorY = div(n[1], m[1], x, y)

    return [coorX, coorY]

# Subdivision Point Formula
def divPoint(n: int, m: int, point) :
    return ((1 - point) * n + point * m)

def subdivPoint(n: tuple[int, int], m: tuple[int, int], point) :
    coorX = divPoint(n[0], m[0], point)
    coorY = divPoint(n[1], m[1], point)


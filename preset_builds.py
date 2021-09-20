def neglider(x, y, alive):
    build = [(x,y), (x-1,y-1), (x-1,y+1), (x,y+1), (x+1,y)]
    alive.update(build)


def nwglider(x, y, alive):
    build = [(x,y), (x+1,y-1), (x+1,y+1), (x,y+1),(x-1,y)]
    alive.update(build)


def seglider(x, y, alive):
    build = [(x,y), (x-1,y+1), (x-1,y-1), (x,y-1), (x+1,y)]
    alive.update(build)


def swglider(x, y, alive):
    build = [(x,y), (x+1,y+1), (x+1,y-1), (x,y-1),(x-1,y)]
    alive.update(build)


def glider_gun(x,y, alive):
    build = [(x-5,y-4), (x-4,y-4), (x-6, y-3), (x-2, y-3), (x-7,y-2), (x-1,y-2), (x+7, y-2), (x-17, y-1), (x-16, y-1),
             (x-7, y-1), (x-3, y-1), (x-1, y-1), (x, y-1), (x+5, y-1), (x+7, y-1), (x-17, y), (x-16, y), (x-7, y),
             (x-1, y), (x+3, y), (x+4, y), (x-6, y+1), (x-2, y+1), (x+3, y+1), (x+4, y+1), (x+17, y+1), (x+18, y+1),
             (x-5, y+2), (x-4, y+2), (x+3, y+2), (x+4, y+2), (x+17, y+2), (x+18, y+2), (x+5, y+3), (x+7, y+3),
             (x+7, y+4)]
    alive.update(build)

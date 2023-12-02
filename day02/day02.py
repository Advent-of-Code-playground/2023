import re
import numpy as np

def proc_set(s):
    cubes = [e.strip().split(" ") for e in s.split(",")]
    cubes = [{c:int(n)} for n, c in cubes]
    return cubes

def read_inp(file_name):
    games = {}
    with open(file_name, 'r') as f:
        for i, line in enumerate(f, 1):
            idx, game = line.strip().split(":")
            sets = game.split(";")
            sets = [proc_set(s) for s in sets]
            games[int(idx.split(" ")[1])] = sets
    return games

def p1():
    possible_cubes = {
        "red"       : 12,
        "green"     : 13,
        "blue"      : 14
    }

    inp = read_inp('day02.dat')
    games = [ndx for ndx, game in inp.items()]
    impossible_games = []
    for ndx, game in inp.items():
        for s in game:
            for cube in s:
                (color, val), *drop = cube.items()
                if val > possible_cubes[color]:
                    impossible_games.append(ndx)
    impossible_games = set(impossible_games)

    
    for i in impossible_games:
        games.remove(i)
    return(sum(games))

def p2():
    inp = read_inp('day02.dat')
    powers = []
    for ndx, game in inp.items():
        min_cubes = {}
        for s in game:
            for cube in s:
                (color, val), *drop = cube.items()
                if color in min_cubes:
                    min_cubes[color] = max(min_cubes[color], val)
                else:
                    min_cubes[color] = val
        print(min_cubes)
        powers.append(np.prod(list(min_cubes.values())))
    return(sum(powers))



print(p2())
import re
import numpy as np
import pandas as pd

def proc_set(s):
    cubes = [e.strip().split(" ") for e in s.split(",")]
    cubes = {c:int(n) for n, c in cubes}
    return cubes

def proc_game(game):
    sets = game.split(";")
    sets = [proc_set(s) for s in sets]
    sets = [pd.DataFrame(s, index=[i]) for i, s in enumerate(sets)]
    sets = pd.concat(sets).fillna(0)
    return sets


def read_inp(file_name):
    games = {}
    with open(file_name, 'r') as f:
        for i, line in enumerate(f, 1):
            idx, game = line.strip().split(":")
            game = proc_game(game)
            games[int(idx.split(" ")[1])] = game
    return games

def p1():
    inp = read_inp('day02.dat')
    possible_cubes = {
        "red"       : 12,
        "green"     : 13,
        "blue"      : 14
    }
    
    impossible_games = []
    for ndx, game in inp.items():
        for c in game.keys():
            if not c in possible_cubes:
                impossible_games.append(ndx)
                break
            elif game[c].max() > possible_cubes[c]:
                impossible_games.append(ndx)
                break
    # impossible_games = set(impossible_games)
    return sum([ndx for ndx in inp.keys() if ndx not in impossible_games])

def p2():
    inp = read_inp('day02.dat')
    powers = []
    for ndx, game in inp.items():
        powers.append(np.prod(game.max().values))
    return int(sum(powers))

if __name__ == "__main__":
    for i, part in enumerate([p1, p2], 1):
        print(f"Part {i} solution: {part()}")
import numpy as np

def read_input(name):
  with open(name, 'r') as input:
    inp = input.readlines()
    inp = list(map(lambda x: x.strip().split(), inp))
    return {
      "time": list(map(int, inp[0][1:])),
      "distance": list(map(int, inp[1][1:])),
    }


'''given time t
given max_d d

Dv = aDt
v = v0 + aDt

DX = vDt
Dx = (v0 + aDt)Dt
x = x0 + v0Dt + aDt^2'''

def get_distance(v, t):
  '''We are assuming x0=0, v0=0, and t0=0'''
  return v * t

def get_wins(total_time, distance):
  wins = [t for t in range(total_time) if (get_distance(t, total_time-t) > distance)]
  return wins

def p1():
  inp = read_input("day06/day06.dat")
  print(inp)
  n_wins = [len(get_wins(t, d)) for t, d in zip(inp["time"], inp["distance"])]
  return np.prod(n_wins)

def p2():
  inp = read_input("day06/day06.dat")
  time = int("".join(np.array(inp["time"]).astype(str)))
  distance = int("".join(np.array(inp["distance"]).astype(str)))
  print(time, distance)
  return len(get_wins(time, distance))

def main():
  print(f"Part1: {p1()}")
  print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()
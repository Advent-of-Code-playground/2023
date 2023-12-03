import re
import numpy as np

def read_input(name):
  with open(name, 'r') as input:
    inp=input.readlines()
  return list(map(lambda x: x.strip(), inp))

def get_symbols(inp):
  symbols = []
  not_symbol = r'([^\d])'
  for l in inp:
    a = [c for c in re.findall(not_symbol, l) if c != '.']
    symbols.extend(a)
  return set(symbols)

class Map:
  def __init__(self, inp):
    self.map = inp
    self.symbols = get_symbols(inp)

  def get_symbol(self):
    return self.symbols
  
  def get_pos(self, row=None, col=None, coord=None):
    if coord and (row or col):
      raise ValueError("Only one of row, col or coord can be given")
    if coord:
      row = coord[0]
      col = coord[1]
    return self.map[row][col]
  
  def get_symbol_pos_list(self):
    pos_list = []
    for i, l in enumerate(self.map):
      for j, c in enumerate(l):
        if c in self.symbols:
          pos_list.append((i, j))
    return pos_list

  def get_number_pos_list(self):
    pos_list = []
    for i, l in enumerate(self.map):
      numbers = [m for m in re.finditer(r'(\d+)', l)]
      pos_list.extend([(i, n) for n in numbers])
    return pos_list

  def __str__(self):
    ret = ""
    for l in self.map:
      ret += l + "\n"
    return ret

def check_overlap(symbol_span, number_span):
  if (number_span[0]>=symbol_span[0]) and (number_span[0]<=symbol_span[1]):
    return True
  if (number_span[1]>=symbol_span[0]) and (number_span[1]<=symbol_span[1]):
    return True
  return False

def visualize(map):
  print(map)
  for s in map.get_symbol_pos_list():
    print(s, map.get_pos(coord=s))
  for l, n in map.get_number_pos_list():
    print((l,n.span()), ''.join([map.get_pos(row=l, col=y) for y in range(n.start(), n.end())]))
    # print((l, n.span()), n.group())

def p1():
  inp = read_input("day03/day03.dat")
  map = Map(inp)
  
  # visualize(map)

  part_numbers = []
  for l, n in map.get_number_pos_list():
    for s in map.get_symbol_pos_list():
      if (l>=s[0]-1) and (l<=s[0]+1):
        symbol_span = (s[1]-1, s[1]+1)
        number_span = (n.start(), n.end()-1)
        if check_overlap(symbol_span, number_span):
          # print(f"Found {n.group()} [{n.start()},{n.end()}] at {s}")
          part_numbers.append(n.group())
          break

  return np.array(part_numbers).astype(int).sum()
      

def p2():
  inp = read_input("day03/day03.dat")
  map = Map(inp)
  
  # visualize(map)

  gear_ratios = []
  for s in map.get_symbol_pos_list():
    if map.get_pos(coord=s) != '*': 
      continue
    n_part_numbers = []
    for l, n in map.get_number_pos_list():
      if (l>=s[0]-1) and (l<=s[0]+1):
        symbol_span = (s[1]-1, s[1]+1)
        number_span = (n.start(), n.end()-1)
        if check_overlap(symbol_span, number_span):
          n_part_numbers.append(n.group())
          # print(f"Found {n.group()} [{n.start()},{n.end()}] at {s}")
    if len(n_part_numbers) == 2:
      gear_ratios.append(np.prod(np.array(n_part_numbers).astype(int)))

  return np.array(gear_ratios).astype(int).sum()


def main():
  print(f"Part1: {p1()}")
  print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()
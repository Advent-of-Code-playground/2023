import re

class Node:
  def __init__(self, name, L, R):
    self.name = name
    self.L = L
    self.R = R
  
  def __repr__(self):
    return f"{self.name}: ({self.L}, {self.R})"
  
  def __str__(self):
    return f"{self.name}: ({self.L}, {self.R})"

def read_input(name):
  with open(name, 'r') as input:
    inp = list(map(lambda x: x.strip(), input.readlines()))
    instructions = inp[0]
    pattern = r'(\w+) = \((\w+), (\w+)\)'
    nodes = {}
    for n in inp[2:]:
      m = re.match(pattern, n)
      node, L, R = m.group(1), m.group(2), m.group(3)
      nodes[node] = Node(node, L, R)
    return instructions, nodes

def p1():
  instructions, grid = read_input("day08.dat")
  steps = 0
  node = "AAA"
  while node != "ZZZ":
    node = grid[node].L if instructions[steps - (steps//len(instructions))*len(instructions)] == "L" else grid[node].R
    steps += 1
  return steps


def p2():
  instructions, grid = read_input("day08.dat")
  
  # Bringing each ghost to Z once
  steps = []
  nodes = [n for n in grid.keys() if n.endswith("A")]
  for n in nodes:
    node = n
    step=0
    while not node.endswith("Z"):
      node = grid[node].L if instructions[step - (step//len(instructions))*len(instructions)] == "L" else grid[node].R
      step += 1
    steps.append(step)
  print(steps)

  #Brute forcing the walk of all ghosts together
  steps = []
  nodes = [n for n in grid.keys() if n.endswith("A")]
  while not all([n.endswith("Z") for n in nodes]):
    print(nodes)
    if instructions[steps - (steps//len(instructions))*len(instructions)] == "L":
      nodes = [grid[node].L for node in nodes]
    else:
      nodes = [grid[node].R for node in nodes]
    steps += 1
  return steps

def main():
  print(f"Part1: {p1()}")
  print(f"Part2: {p2()}") # Maybe 9606140307013 if I accept to cheat and use LMC just for the lulz

if __name__ == "__main__":
  main()
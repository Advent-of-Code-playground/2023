from collections import defaultdict 

def read_input(name):
  print(f"Reading {name}")
  with open(name, 'r') as input:
    seeds = []
    chain_dicts = defaultdict(dict)
    for line in input:
      if "seeds" in line:
        seeds = list(map(int,line.split(":")[1].strip().split()))
        print(f"seeds: {seeds}")
      else:
        if "map" in line:
          source = line.split(" ")[0].split("-")[0]
          destination = line.split(" ")[0].split("-")[2]
          chain_dicts[f"{source}->{destination}"] = defaultdict(lambda x: x)
          print(f"{source}->{destination}")
          content_line = input.readline()
          while content_line.strip():
            destination_val, source_val, length_val = list(map(int,content_line.split()))
            print(f"{source_val} -> {destination_val} ({length_val})")
            for l in range(length_val):
              print(l)
              chain_dicts[f"{source}->{destination}"][source_val+l] = destination_val+l
            content_line = input.readline()
    
  return seeds, chain_dicts

def get_next_destination(source, chain_dicts):
  for key in chain_dicts.keys():
    if key.startswith(source):
      return key.split("->")[1]
  

def get_location(seed, chain_dicts):
  destination = "seed"
  source_val = seed
  while destination != "location":
    source = destination
    destination = get_next_destination(destination, chain_dicts)
    source_val = chain_dicts[f'{source}->{destination}'].get(source_val, source_val)
  return source_val



    # source = chain_dicts[source][source_val]
    # source_val = source

def p1():
  seeds, chain_dicts = read_input("2023/day05/day05.dat")
  # print(chain_dicts.keys())

  # print(seeds)
  # print([(s, get_location(s, chain_dicts)) for s in seeds])
  return sorted([(s, get_location(s, chain_dicts)) for s in seeds], key=lambda x: x[1])[0][1]



def p2():
  pass

def main():
  print(f"Part1: {p1()}")
  print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()
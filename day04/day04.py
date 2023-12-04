

def read_input(name):
  with open(name, 'r') as input:
    inp = input.readlines()
    inp = list(map(lambda x: x.split(":")[1], inp))
    inp = list(map(lambda x: x.strip(), inp))
    winning_list = list(map(lambda x: x.split("|")[0].split(), inp))
    personal_list = list(map(lambda x: x.split("|")[1].split(), inp))
  return (
    [list(map(int, w)) for w in winning_list], 
    [list(map(int, p)) for p in personal_list]
    )

def p1():
  (winning_list, personal_list) = read_input("day04/day04.dat")
  total_points = 0
  for cards in zip(winning_list, personal_list):
    winning = cards[0]
    personal = cards[1]
    points = [n for n in personal if n in winning]
    if points:
      total_points += 2**(len(points)-1)
  return total_points


def p2():
  (winning_list, personal_list) = read_input("day04/day04.dat")
  points_per_card = []
  number_of_copies = []
  for cards in zip(winning_list, personal_list):
    winning = cards[0]
    personal = cards[1]
    points_per_card.append(len([n for n in personal if n in winning]))
    number_of_copies.append(1)
  for i, (p, n) in enumerate(zip(points_per_card, number_of_copies)):
    for c in range(1, p+1):
      number_of_copies[i+c] += n
  return sum(number_of_copies)

def main():
  # print(f"Part1: {p1()}")
  print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()
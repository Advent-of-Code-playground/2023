

def read_input(name):
  with open(name, 'r') as input:
    inp = tuple(map(lambda x: x.strip().split(), input.readlines()))
    return inp

class Hand:
  def __init__(self, hand, bid):
    self.points = {
      "five_of_a_kind" : 6,
      "four_of_a_kind" : 5,
      "full_house" : 4,
      "three_of_a_kind" : 3,
      "two_pairs" : 2,
      "one_pair" : 1,
      "high_card" : 0,
    }

    self.cards_points = {
      "A" : 14,
      "K" : 13,
      "Q" : 12,
      "J" : 11,
      "T" : 10,
      "9" : 9,
      "8" : 8,
      "7" : 7,
      "6" : 6,
      "5" : 5,
      "4" : 4,
      "3" : 3,
      "2" : 2,
    }
    if len(hand) != 5:
      raise ValueError("Hand must contain 5 cards")
    if any([c not in self.cards_points for c in hand]):
      raise ValueError("Hand contains invalid card")
    self.hand = hand
    self.bid = int(bid)


  def get_strength(self):
    unique = set(self.hand)
    count_unique = [self.hand.count(u) for u in unique]
    if 5 in count_unique:
      return "five_of_a_kind"
    elif 4 in count_unique:
      return "four_of_a_kind"
    elif 3 in count_unique:
      if 2 in count_unique:
        return "full_house"
      else:
        return "three_of_a_kind"
    elif 2 in count_unique:
      if count_unique.count(2) == 2:
        return "two_pairs"
      else:
        return "one_pair"
    else:
      return "high_card"

  def get_rank(self):
    return self.points[self.get_strength()]

  def __gt__(self, other):
    rank_self = self.get_rank()
    rank_other = other.get_rank()
    if rank_self != rank_other:
      return rank_self > rank_other
    else:
      for s, o in zip(self.hand, other.hand):
        if s != o:
          return self.cards_points[s] > self.cards_points[o]
    # return False

  def __eq__(self, other):
    return self.hand == other.hand

  def __repr__(self):
    return f"{self.hand} ({self.bid})"

  def __str__(self):
    return f"{self.hand} ({self.bid})"

class Hand_2(Hand):
    def __init__(self, hand, bid):
      super().__init__(hand, bid)
      self.cards_points = {
        "A" : 14,
        "K" : 13,
        "Q" : 12,
        "T" : 10,
        "9" : 9,
        "8" : 8,
        "7" : 7,
        "6" : 6,
        "5" : 5,
        "4" : 4,
        "3" : 3,
        "2" : 2,
        "J" : 1,
      }

    def get_rank(self):
      original_hand = self.hand
      possible_strengths = []
      for k in self.cards_points.keys():
        self.hand = self.hand.replace("J", k)
        possible_strengths.append(super().get_rank())
        self.hand = original_hand
      return max(possible_strengths)

def p1():
  inp = read_input("day07/day07.dat")
  hands = [Hand(h[0], h[1]) for h in inp]
  # print(sorted(hands)) #252783048 <- reverse order
  return sum([h.bid*p for p, h in enumerate(sorted(hands), 1)])


def p2():
  inp = read_input("day07/day07.dat")
  hands = [Hand_2(h[0], h[1]) for h in inp]
  return sum([h.bid*p for p, h in enumerate(sorted(hands), 1)])

def main():
  print(f"Part1: {p1()}")
  print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()
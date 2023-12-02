import re
import numpy as np

def read_inp(file_name):
    with open(file_name, 'r') as f:
        inp = f.readlines()
    return inp

dict = {
    'one'   : '1',
    'two'   : '2',
    'three' : '3',
    'four'  : '4',
    'five'  : '5',
    'six'   : '6',
    'seven' : '7',
    'eight' : '8',
    'nine'  : '9',
    'zero'  : '0',
    '1'     : '1',
    '2'     : '2',
    '3'     : '3',
    '4'     : '4',
    '5'     : '5',
    '6'     : '6',
    '7'     : '7',
    '8'     : '8',
    '9'     : '9',
    '0'     : '0',
}

# Sol1
pattern1 = r'\d'
#Sol2
pattern2 = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

print([k for k in re.findall(pattern2,'zoneight234')])

inp = read_inp("day01.dat")

for i, p in enumerate([pattern1, pattern2], 1):
  digits = [
        (
          dict[re.findall(p, line)[0]]+dict[re.findall(p, line)[-1]]
        )
      for line in inp
      ]

  digits = np.array(digits).astype(int)
  print(f"Part {i} solution: {digits.sum()}")



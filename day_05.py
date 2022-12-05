import re
import copy

real_input = """
            [M] [S] [S]            
        [M] [N] [L] [T] [Q]        
[G]     [P] [C] [F] [G] [T]        
[B]     [J] [D] [P] [V] [F] [F]    
[D]     [D] [G] [C] [Z] [H] [B] [G]
[C] [G] [Q] [L] [N] [D] [M] [D] [Q]
[P] [V] [S] [S] [B] [B] [Z] [M] [C]
[R] [H] [N] [P] [J] [Q] [B] [C] [F]
 1   2   3   4   5   6   7   8   9 

move 1 from 7 to 4
move 3 from 4 to 7
move 4 from 3 to 4
move 5 from 6 to 9
move 1 from 8 to 1
move 2 from 3 to 2
move 3 from 4 to 6
move 1 from 3 to 6
move 9 from 7 to 1
move 1 from 2 to 4
move 3 from 4 to 9
move 4 from 9 to 8
move 6 from 8 to 2
move 1 from 8 to 6
move 1 from 4 to 1
move 11 from 1 to 7
move 1 from 4 to 7
move 7 from 2 to 5
move 5 from 6 to 3
move 2 from 4 to 3
move 2 from 5 to 9
move 1 from 8 to 6
move 3 from 1 to 5
move 2 from 6 to 9
move 1 from 4 to 8
move 2 from 2 to 1
move 7 from 5 to 9
move 6 from 3 to 6
move 1 from 2 to 5
move 1 from 3 to 8
move 12 from 7 to 3
move 1 from 1 to 8
move 2 from 1 to 9
move 20 from 9 to 5
move 1 from 1 to 7
move 5 from 5 to 3
move 1 from 8 to 7
move 2 from 8 to 3
move 2 from 6 to 5
move 1 from 6 to 4
move 18 from 3 to 2
move 1 from 4 to 2
move 1 from 7 to 9
move 1 from 1 to 9
move 1 from 6 to 1
move 8 from 5 to 2
move 1 from 1 to 6
move 19 from 5 to 2
move 5 from 2 to 6
move 2 from 9 to 7
move 20 from 2 to 1
move 1 from 9 to 4
move 8 from 6 to 2
move 5 from 1 to 3
move 27 from 2 to 1
move 34 from 1 to 7
move 1 from 2 to 6
move 2 from 3 to 1
move 1 from 4 to 9
move 1 from 2 to 6
move 2 from 1 to 7
move 1 from 6 to 7
move 1 from 9 to 3
move 2 from 6 to 3
move 1 from 6 to 4
move 5 from 3 to 4
move 5 from 4 to 2
move 4 from 1 to 4
move 4 from 1 to 4
move 2 from 3 to 6
move 1 from 6 to 9
move 25 from 7 to 5
move 1 from 6 to 4
move 17 from 5 to 2
move 14 from 7 to 6
move 1 from 7 to 3
move 1 from 9 to 3
move 10 from 2 to 3
move 2 from 2 to 9
move 12 from 3 to 5
move 18 from 5 to 8
move 1 from 4 to 2
move 5 from 2 to 1
move 1 from 5 to 3
move 3 from 2 to 1
move 1 from 2 to 7
move 2 from 2 to 6
move 9 from 6 to 7
move 16 from 8 to 2
move 6 from 7 to 3
move 2 from 8 to 9
move 1 from 1 to 8
move 16 from 2 to 6
move 1 from 8 to 3
move 2 from 1 to 2
move 1 from 9 to 3
move 7 from 4 to 1
move 7 from 3 to 7
move 9 from 7 to 8
move 1 from 5 to 6
move 2 from 9 to 7
move 1 from 9 to 5
move 11 from 6 to 8
move 1 from 3 to 1
move 1 from 4 to 2
move 2 from 8 to 5
move 3 from 5 to 8
move 2 from 1 to 9
move 5 from 1 to 4
move 3 from 4 to 1
move 1 from 3 to 2
move 3 from 2 to 1
move 1 from 9 to 1
move 1 from 2 to 5
move 2 from 4 to 7
move 20 from 8 to 5
move 1 from 9 to 7
move 11 from 6 to 1
move 17 from 1 to 5
move 1 from 8 to 2
move 7 from 5 to 8
move 1 from 4 to 5
move 2 from 1 to 2
move 2 from 8 to 4
move 4 from 7 to 6
move 2 from 6 to 8
move 2 from 1 to 2
move 1 from 1 to 4
move 4 from 8 to 9
move 2 from 1 to 9
move 3 from 8 to 1
move 25 from 5 to 2
move 23 from 2 to 1
move 1 from 7 to 1
move 6 from 9 to 8
move 6 from 8 to 3
move 3 from 6 to 2
move 10 from 1 to 2
move 1 from 6 to 3
move 2 from 3 to 6
move 2 from 3 to 2
move 2 from 6 to 8
move 1 from 4 to 6
move 14 from 1 to 9
move 2 from 3 to 4
move 14 from 2 to 4
move 1 from 6 to 9
move 17 from 4 to 3
move 1 from 8 to 6
move 2 from 7 to 2
move 1 from 4 to 2
move 1 from 5 to 9
move 9 from 2 to 4
move 17 from 3 to 7
move 3 from 4 to 2
move 1 from 8 to 3
move 4 from 5 to 7
move 1 from 3 to 6
move 1 from 4 to 5
move 14 from 7 to 9
move 2 from 1 to 9
move 3 from 2 to 1
move 1 from 2 to 5
move 1 from 3 to 7
move 4 from 1 to 2
move 2 from 6 to 7
move 3 from 9 to 8
move 4 from 2 to 4
move 17 from 9 to 7
move 1 from 2 to 8
move 8 from 9 to 6
move 1 from 8 to 2
move 19 from 7 to 9
move 9 from 4 to 2
move 5 from 7 to 3
move 3 from 5 to 9
move 6 from 2 to 5
move 1 from 9 to 4
move 3 from 2 to 9
move 25 from 9 to 5
move 1 from 3 to 6
move 2 from 5 to 8
move 6 from 6 to 7
move 1 from 3 to 4
move 2 from 3 to 4
move 1 from 8 to 2
move 2 from 2 to 9
move 2 from 8 to 3
move 5 from 7 to 6
move 3 from 7 to 9
move 7 from 5 to 8
move 2 from 3 to 5
move 1 from 3 to 5
move 1 from 6 to 2
move 6 from 9 to 5
move 1 from 9 to 2
move 1 from 6 to 9
move 2 from 5 to 6
move 2 from 9 to 8
move 11 from 8 to 1
move 2 from 5 to 9
move 3 from 6 to 5
move 1 from 4 to 7
move 5 from 5 to 7
move 1 from 4 to 8
move 7 from 7 to 2
move 12 from 5 to 2
move 10 from 1 to 8
move 1 from 9 to 6
move 3 from 8 to 1
move 1 from 1 to 6
move 10 from 2 to 3
move 8 from 8 to 7
move 1 from 9 to 8
move 2 from 3 to 5
move 14 from 5 to 8
move 1 from 3 to 2
move 3 from 8 to 1
move 3 from 8 to 4
move 3 from 2 to 4
move 5 from 6 to 4
move 8 from 7 to 9
move 6 from 8 to 7
move 1 from 5 to 7
move 6 from 2 to 9
move 4 from 4 to 6
move 4 from 4 to 9
move 3 from 9 to 3
move 1 from 8 to 6
move 1 from 5 to 6
move 2 from 7 to 2
move 1 from 3 to 4
move 3 from 4 to 1
move 3 from 4 to 3
move 5 from 6 to 4
move 4 from 3 to 8
move 1 from 6 to 4
move 8 from 3 to 2
move 2 from 8 to 5
move 11 from 9 to 7
move 9 from 1 to 9
move 2 from 7 to 3
move 1 from 6 to 8
move 1 from 6 to 5
move 5 from 9 to 8
move 3 from 9 to 7
move 2 from 9 to 1
move 2 from 3 to 7
move 12 from 7 to 1
move 2 from 8 to 9
move 5 from 4 to 5
move 4 from 9 to 4
move 1 from 1 to 3
move 7 from 1 to 3
move 7 from 5 to 6
move 1 from 9 to 1
move 1 from 5 to 1
move 5 from 7 to 8
move 4 from 6 to 7
move 5 from 1 to 8
move 1 from 4 to 3
move 12 from 8 to 7
move 2 from 2 to 4
move 2 from 8 to 9
move 3 from 8 to 2
move 2 from 6 to 7
move 4 from 7 to 8
move 1 from 6 to 8
move 4 from 3 to 2
move 15 from 7 to 8
move 1 from 7 to 6
move 3 from 3 to 5
move 2 from 3 to 4
move 5 from 2 to 5
move 3 from 1 to 5
move 4 from 5 to 6
move 4 from 5 to 9
move 1 from 5 to 7
move 4 from 9 to 4
move 2 from 2 to 9
move 2 from 5 to 2
move 2 from 2 to 1
move 3 from 4 to 9
move 2 from 9 to 4
move 2 from 8 to 5
move 2 from 5 to 2
move 8 from 2 to 4
move 2 from 1 to 3
move 2 from 3 to 5
move 3 from 6 to 9
move 2 from 6 to 1
move 2 from 1 to 4
move 1 from 2 to 4
move 1 from 5 to 7
move 2 from 2 to 7
move 18 from 4 to 2
move 1 from 5 to 9
move 2 from 7 to 9
move 18 from 8 to 4
move 1 from 7 to 8
move 22 from 4 to 8
move 6 from 2 to 6
move 3 from 6 to 8
move 3 from 6 to 4
move 3 from 4 to 7
move 3 from 7 to 1
move 14 from 2 to 3
move 10 from 3 to 2
move 27 from 8 to 1
move 1 from 7 to 6
move 1 from 3 to 7
move 2 from 2 to 8
move 2 from 9 to 8
move 18 from 1 to 4
move 6 from 1 to 5
move 10 from 4 to 7
move 1 from 3 to 7
move 4 from 7 to 2
move 3 from 9 to 7
move 1 from 6 to 5
move 1 from 2 to 7
move 2 from 5 to 6
move 2 from 6 to 5
move 3 from 5 to 1
move 6 from 1 to 3
move 4 from 5 to 9
move 11 from 2 to 9
move 2 from 1 to 6
move 3 from 4 to 6
move 5 from 7 to 3
move 2 from 6 to 1
move 2 from 1 to 5
move 1 from 8 to 2
move 1 from 1 to 8
move 1 from 6 to 4
move 2 from 4 to 5
move 4 from 5 to 9
move 11 from 3 to 6
move 1 from 3 to 6
move 8 from 6 to 5
move 1 from 3 to 5
move 4 from 4 to 8
move 21 from 9 to 6
move 2 from 9 to 5
move 1 from 9 to 3
move 1 from 2 to 6
move 7 from 8 to 6
move 12 from 6 to 5
move 1 from 8 to 2
move 10 from 6 to 7
move 15 from 7 to 2
move 2 from 7 to 3
move 13 from 6 to 8
move 9 from 5 to 1
move 12 from 5 to 3
move 1 from 2 to 3
move 1 from 9 to 7
move 9 from 3 to 4
move 3 from 4 to 6
move 1 from 7 to 6
move 6 from 4 to 1
move 2 from 5 to 2
move 6 from 1 to 8
move 9 from 8 to 6
move 7 from 3 to 2
move 1 from 2 to 9
move 9 from 6 to 1
move 13 from 1 to 7
move 4 from 8 to 5
move 2 from 7 to 1
move 3 from 6 to 4
move 3 from 5 to 8
move 3 from 2 to 6
move 1 from 5 to 3
move 1 from 3 to 4
move 1 from 9 to 8
move 3 from 8 to 7
move 12 from 2 to 9
move 10 from 7 to 4
move 5 from 8 to 4
move 1 from 8 to 5
move 11 from 4 to 7
move 8 from 9 to 7
move 1 from 6 to 2
move 8 from 2 to 6
move 1 from 5 to 8
move 4 from 1 to 5
move 4 from 9 to 6
move 3 from 1 to 3
move 2 from 8 to 4
move 1 from 7 to 6
move 1 from 2 to 7
move 2 from 3 to 7
move 4 from 4 to 9
move 11 from 6 to 9
move 10 from 7 to 8
move 1 from 3 to 4
move 1 from 6 to 4
move 4 from 5 to 7
move 6 from 7 to 4
move 1 from 8 to 7
move 4 from 6 to 7
move 12 from 4 to 8
move 12 from 8 to 1
move 1 from 8 to 2
move 10 from 1 to 7
move 2 from 4 to 1
move 8 from 8 to 3
move 4 from 1 to 6
move 8 from 7 to 6
move 2 from 6 to 5
move 2 from 5 to 2
move 13 from 9 to 3
move 3 from 2 to 5
move 8 from 3 to 4
move 7 from 6 to 7
move 1 from 9 to 2
move 1 from 9 to 1
move 2 from 6 to 4
move 3 from 4 to 8
move 1 from 1 to 7
move 4 from 4 to 6
move 3 from 8 to 7
move 1 from 2 to 9
move 1 from 5 to 2
move 1 from 2 to 5
move 2 from 4 to 5
move 1 from 7 to 2
move 13 from 3 to 4
move 7 from 4 to 3
move 4 from 5 to 9
move 1 from 4 to 7
move 5 from 6 to 3
move 3 from 9 to 7
move 10 from 7 to 8
move 3 from 4 to 8
move 1 from 5 to 4
move 2 from 3 to 1
move 3 from 7 to 4
move 4 from 8 to 6
move 2 from 9 to 3
move 2 from 4 to 5
move 4 from 4 to 3
move 8 from 8 to 3
move 3 from 6 to 8
move 1 from 2 to 6
move 5 from 7 to 9
move 1 from 4 to 3
move 3 from 7 to 5
move 3 from 8 to 4
move 7 from 7 to 5
move 3 from 7 to 8
move 1 from 9 to 8
move 3 from 4 to 1
move 1 from 5 to 8
move 3 from 7 to 1
move 6 from 8 to 3
move 3 from 9 to 5
move 2 from 6 to 5
move 2 from 1 to 6
move 16 from 3 to 8
move 4 from 5 to 8
move 4 from 3 to 8
move 1 from 9 to 5
move 1 from 6 to 5
move 3 from 3 to 7
move 6 from 1 to 6
move 1 from 5 to 4
move 3 from 5 to 2
move 2 from 7 to 4
move 1 from 2 to 8
move 6 from 8 to 1
move 2 from 4 to 5
move 2 from 2 to 3
move 7 from 8 to 7
move 1 from 4 to 6
move 3 from 6 to 4
move 3 from 4 to 9
move 3 from 6 to 3
move 11 from 8 to 6
move 12 from 5 to 4
move 5 from 6 to 1
move 9 from 3 to 2
move 7 from 6 to 1
move 7 from 7 to 8
move 5 from 8 to 3
move 2 from 3 to 6
move 2 from 8 to 1
move 1 from 7 to 2
move 7 from 3 to 8
move 1 from 9 to 1
move 14 from 1 to 3
move 9 from 2 to 8
move 11 from 3 to 4
move 22 from 4 to 1
move 2 from 3 to 1
move 16 from 8 to 4
move 1 from 9 to 2
move 3 from 6 to 9
move 3 from 9 to 5
move 1 from 2 to 6
move 1 from 5 to 7
"""

sample_input = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

crates = []
prod = True
if prod:
  input = real_input
  crates = [['R','P','C','D','B','G'],['H','V','G'],['N','S','Q','D','J','P','M'],['P','S','L','G','D','C','N','M'],['J','B','N','C','P','F','L','S'],['Q','B','D','Z','V','G','T','S'],['B','Z','M','H','F','T','Q'],['C','M','D','B','F'],['F','C','Q','G']]
else:
  input = sample_input
  crates = [['Z','N'],['M','C','D'],['P']]

star1 = ""
star2 = ""

crate_data = copy.deepcopy(crates)
for line in input.strip().split("\n"):
  if matches := re.search(r"move (\d+) from (\d+) to (\d+)", line):
    move_quantity = int(matches.group(1))
    move_from = int(matches.group(2))
    move_to = int(matches.group(3))
    crate_set = []
    for n in range(0,move_quantity):
      crate_data[move_to-1].append((crate_data[move_from-1].pop()))

for crate in crate_data:
  star1 += crate[-1]

crate_data = copy.deepcopy(crates)
for line in input.strip().split("\n"):
  if matches := re.search(r"move (\d+) from (\d+) to (\d+)", line):
    move_quantity = int(matches.group(1))
    move_from = int(matches.group(2))
    move_to = int(matches.group(3))
    crate_set = []
    for n in range(0,move_quantity):
      crate_set.append(crate_data[move_from-1].pop())

    crate_set.reverse()
    crate_data[move_to-1].extend(crate_set)

for crate in crate_data:
  star2 += crate[-1]

print("star 1: ", star1)
print("star 2: ", star2)
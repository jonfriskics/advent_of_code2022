real_input = """
noop
noop
noop
addx 3
addx 20
noop
addx -12
noop
addx 4
noop
noop
noop
addx 1
addx 2
addx 5
addx 16
addx -14
addx -25
addx 30
addx 1
noop
addx 5
noop
addx -38
noop
noop
noop
addx 3
addx 2
noop
noop
noop
addx 5
addx 5
addx 2
addx 13
addx 6
addx -16
addx 2
addx 5
addx -15
addx 16
addx 7
noop
addx -2
addx 2
addx 5
addx -39
addx 4
addx -2
addx 2
addx 7
noop
addx -2
addx 17
addx -10
noop
noop
addx 5
addx -1
addx 6
noop
addx -2
addx 5
addx -8
addx 12
addx 3
addx -2
addx -19
addx -16
addx 2
addx 5
noop
addx 25
addx 7
addx -29
addx 3
addx 4
addx -4
addx 9
noop
addx 2
addx -20
addx 23
addx 1
noop
addx 5
addx -10
addx 14
addx 2
addx -1
addx -38
noop
addx 20
addx -15
noop
addx 7
noop
addx 26
addx -25
addx 2
addx 7
noop
noop
addx 2
addx -5
addx 6
addx 5
addx 2
addx 8
addx -3
noop
addx 3
addx -2
addx -38
addx 13
addx -6
noop
addx 1
addx 5
noop
noop
noop
noop
addx 2
noop
noop
addx 7
addx 3
addx -2
addx 2
addx 5
addx 2
noop
addx 1
addx 5
noop
noop
noop
noop
noop
noop
"""

sample_input = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

prod = True
if prod:
  input = real_input
else:
  input = sample_input

star1 = 0
star2 = 0

cycle = 0
x = 1

for line in input.strip().split("\n"):
  if line[0] == 'n':
    cycle += 1
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
      star1 += (cycle * x)
  else:
    value = int(line.split(' ')[1])
    cycle += 1
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
      star1 += (cycle * x)
    cycle += 1
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
      star1 += (cycle * x)
    x += value

def print_grid(grid):
  for l in range(len(grid)):
    print(grid[l].replace('.',' '))
  print("\n---\n")

grid = []

for y in range(0,6):
  dots = [str('.') for n in range(0,40)]
  dots = ''.join(dots)
  grid.append(dots)

cycle = 1
sprite_middle = 1
row = 0

for line in input.strip().split("\n"):
  if line[0] == 'n':
    
    # check sprite against current cycle
    grid_pos = (cycle - 1) % 40
    if sprite_middle - 1 == grid_pos or sprite_middle == grid_pos or sprite_middle + 1 == grid_pos:
      grid[row] = grid[row][:grid_pos] + '#' + grid[row][grid_pos+1:]

    cycle += 1
    if cycle % 40 == 0:
      row += 1

  else:
    value = int(line.split(' ')[1])

    # check sprite position against current cycle
    grid_pos = (cycle - 1) % 40
    if sprite_middle - 1 == grid_pos or sprite_middle == grid_pos or sprite_middle + 1 == grid_pos:
      grid[row] = grid[row][:grid_pos] + '#' + grid[row][grid_pos+1:]

    cycle += 1
    if cycle % 40 == 0:
      row += 1

    # check sprite position after cycle is incremented once
    grid_pos = (cycle - 1) % 40
    if sprite_middle - 1 == grid_pos or sprite_middle == grid_pos or sprite_middle + 1 == grid_pos:
      grid[row] = grid[row][:grid_pos] + '#' + grid[row][grid_pos+1:]
    cycle += 1
    if cycle % 40 == 0:
      row += 1

    # finish executing addr
    sprite_middle += value

print("star 1: ", star1)
print("star 2: ")
print_grid(grid)
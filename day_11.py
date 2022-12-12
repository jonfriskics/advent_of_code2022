import re
import math

real_input = """
Monkey 0:
  Starting items: 50, 70, 54, 83, 52, 78
  Operation: new = old * 3
  Test: divisible by 11
    If true: throw to monkey 2
    If false: throw to monkey 7

Monkey 1:
  Starting items: 71, 52, 58, 60, 71
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 0
    If false: throw to monkey 2

Monkey 2:
  Starting items: 66, 56, 56, 94, 60, 86, 73
  Operation: new = old + 1
  Test: divisible by 3
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 3:
  Starting items: 83, 99
  Operation: new = old + 8
  Test: divisible by 5
    If true: throw to monkey 6
    If false: throw to monkey 4

Monkey 4:
  Starting items: 98, 98, 79
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 1
    If false: throw to monkey 0

Monkey 5:
  Starting items: 76
  Operation: new = old + 4
  Test: divisible by 13
    If true: throw to monkey 6
    If false: throw to monkey 3

Monkey 6:
  Starting items: 52, 51, 84, 54
  Operation: new = old * 17
  Test: divisible by 19
    If true: throw to monkey 4
    If false: throw to monkey 1

Monkey 7:
  Starting items: 82, 86, 91, 79, 94, 92, 59, 94
  Operation: new = old + 7
  Test: divisible by 2
    If true: throw to monkey 5
    If false: throw to monkey 3
"""

sample_input = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

prod = True
if prod:
  input = real_input
else:
  input = sample_input

star1 = 0
star2 = 0

monkeys = {}

for monkey_instructions in input.strip().split("\n\n"):
  monkey_number = None
  starting_items = None
  operation_new = None
  operation_left = None
  operation_type = None
  operation_right = None
  divisible_by = None
  true_throw_to = None
  false_throw_to = None
  for line in monkey_instructions.strip().split("\n"):
    if line.strip()[0:4] == 'Monk':
      monkey_number = line.split(" ")[1].rstrip(':')
      # print(monkey_number)
      monkeys[monkey_number] = {}
    elif line.strip()[0:4] == 'Star':
      starting_items = re.findall(r'(\d+)', line.split(": ")[1])
      starting_items = [int(item) for item in starting_items]
      # print(starting_items)
    elif line.strip()[0:4] == 'Oper':
      operation_match = re.search(r'(.+)\s\=\s(.+)\s(.)\s(.+)', line.split(": ")[1])
      operation_new = operation_match.group(1)
      operation_left = operation_match.group(2)
      operation_type = operation_match.group(3)
      operation_right = operation_match.group(4)
      # print(operation_new, operation_left, operation_type, operation_right)
    elif line.strip()[0:4] == 'Test':
      # print("IN TEST line I'm checking " + line)
      divisible_by = re.search(r'divisible by (\d+)', line.strip())
      divisible_by = divisible_by.group(1)
      # print(divisible_by)
    elif line.strip()[0:4] == 'If t':
      true_throw_to = re.search(r'(\d+)',line.strip())
      true_throw_to = true_throw_to.group(1)
      # print(true_throw_to)
    elif line.strip()[0:4] == 'If f':
      false_throw_to = re.search(r'(\d+)',line.strip())
      false_throw_to = false_throw_to.group(1)
      # print(false_throw_to)

  # print(f'monkey_number {monkey_number} starting_items {starting_items} monkeys {monkeys}')
  monkeys[monkey_number]['starting_items'] = starting_items
  monkeys[monkey_number]['operation_new'] = operation_new
  monkeys[monkey_number]['operation_left'] = operation_left
  monkeys[monkey_number]['operation_type'] = operation_type
  monkeys[monkey_number]['operation_right'] = operation_right
  monkeys[monkey_number]['divisible_by'] = divisible_by
  monkeys[monkey_number]['true_throw_to'] = true_throw_to
  monkeys[monkey_number]['false_throw_to'] = false_throw_to
  monkeys[monkey_number]['inspection_count'] = 0

# print(monkeys)

round_target = 20

while round_target > 0:
  print('current_round ',round_target)
  for monkey in monkeys:
    # print(f'monkey {monkey} values {monkeys[monkey]}')
    # print("---")
    positions_to_remove = []
    pos = 0
    for item in monkeys[monkey]['starting_items']:
      monkeys[monkey]['inspection_count'] += 1
      # print(f'monkey {monkey} item {item}')
      item = int(item)
      worry_level = item
      if monkeys[monkey]['operation_type'] == '+':
        if(monkeys[monkey]['operation_right'] == 'old'):
          worry_level = item + item
        else:
          worry_level = item + int(monkeys[monkey]['operation_right'])
      elif monkeys[monkey]['operation_type'] == '*':
        if(monkeys[monkey]['operation_right'] == 'old'):
          worry_level = item * item
        else:
          worry_level = item * int(monkeys[monkey]['operation_right'])
      worry_level = math.floor(worry_level / 3)

      if worry_level % int(monkeys[monkey]['divisible_by']) == 0:
        monkeys[monkeys[monkey]['true_throw_to']]['starting_items'].append(worry_level)
      else:
        monkeys[monkeys[monkey]['false_throw_to']]['starting_items'].append(worry_level)
    monkeys[monkey]['starting_items'] = []
  round_target -= 1

# print(monkeys)
inspection_counts = []
for monkey in monkeys:
  inspection_counts.append(monkeys[monkey]['inspection_count'])

inspection_counts.sort()
# print(inspection_counts)

star1 = inspection_counts[-1] * inspection_counts[-2]

print("star 1: ", star1)
print("star 2: ", star2)
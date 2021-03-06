# https://adventofcode.com/2021/day/2#part2
# What do you get if you multiply your final horizontal position by your final depth?
# Similar to part 1, but we introduce a intermediate value which is `aim` to hold temporary value
# Final values (horizon and depth) are updated whenever encountering `forward` command
def solve(commands):
  horizontal_pos = 0
  depth_pos = 0
  aim = 0

  for command in commands:
    c, unit = command.split()
    unit = int(unit)

    if c == 'forward':
      horizontal_pos += unit
      depth_pos += aim * unit
    elif c == 'up':
      aim -= unit
    elif c == 'down':
      aim += unit
    else:
      print("Invalid command")
      # Skip it

  return horizontal_pos * depth_pos


if __name__ == '__main__':
  f = open('input.txt')
  planned_course = f.readlines()

  res = solve(planned_course)
  print(res)

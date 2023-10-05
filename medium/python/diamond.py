rows = 10

for row in range(rows):
  print(' ' * (rows - row - 1) + '*' * (2 * row + 1))
for row in range(rows - 2, -1, -1):
  print(' ' * (rows - row - 1) + '*' * (2 * row + 1))
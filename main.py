from math import factorial

#hehehhehehe look i forked and connected to replit

row_length = 50
num_set = [1, 2, 3, 4]

def F(n , k):
  # Partitions = {}

  if k > n:
    k = n
  if n == 1:
    return [1]
  if k == 0 or n == 0:
    return []
  
  l_val = max([x for x in num_set if x <= k])
  if l_val == 1:
    return [1]*n
  nl_val = max([x for x in num_set if x < l_val])

  part = []
  for i in range(n // l_val +1):
    # print(n - l_val * i, nl_val)
    part_before = F(n - l_val * i, nl_val)
    if not part_before:
      part.append([l_val] * i)
    elif isinstance(part_before[0], int):
      part.append([l_val] * i + part_before)
    else:  
      for p in part_before:
        part.append([l_val] * i + p) 

  if len(part) == 1:
    part = part[0]
  return part

def calc_tilings(partition):
  counts = [partition.count(i) for i in num_set]
  n = len(partition)
  num_tilings = factorial(n)
  for val in counts:
    num_tilings //= factorial(val) 
  return num_tilings

partitions = F(row_length, row_length)

total_tilings = 0
for pt in partitions:
  total_tilings += calc_tilings(pt)

print("Total number of tilings = {}".format(total_tilings))
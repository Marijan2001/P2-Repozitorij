def get_even(start, end):
  result = []
  for i in range (start, end +1):
    if i % 2 != 0:
      yield(i)

for num in get_even(1, 100):
  print(num)

def get_odds(start, end):
  result = []
  for i in range (start, end +1):
    if i % 2 != 0:
      yield(i)

for num in get_odds(1, 100):
  print(num)

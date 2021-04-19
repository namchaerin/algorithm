def reverse(number):
  number = str(number)[::-1]
  if number[-1] == '-':
    number = '-' + number[:-1]
  return int(number)
x1 = 1234   # 4321
x2 = -1234  # -4321
x3 = 1230   # 321

def reverse(number):
  # 여기에 코드를 작성해주세요.
  number = str(number)[::-1]
  if number[-1] == '-':
    number = '-' + number[:-1]
  return int(number)

print(reverse(x1))
print(reverse(x2))
print(reverse(x3))


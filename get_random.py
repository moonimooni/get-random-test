import random

def get_zero_or_one():
  return random.randint(0,1)


def get_random(max_num):
  num = max_num

  # change decimal max num to binary
  max_bin = ""
  while num >= 1:
    if num == 1:
      max_bin = "1" + max_bin
      break
    num, left_num = num // 2, num % 2
    max_bin = str(left_num) + max_bin

  if not max_bin:
    return num

  while True:
    # fill list of max_binary length with 0, 1 by random
    random_bin_elements = [get_zero_or_one() for _ in range(len(max_bin))]

    # change binary to decimal and compare original max_num
    decimal = 0
    for i in range(len(random_bin_elements[::-1])):
      if random_bin_elements[i] == 1:
        decimal += (2**i)

    if decimal <= max_num:
      return decimal
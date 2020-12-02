import re

def password_correct_range(pwd, char, min, max):
  count = 0
  for c in pwd:
    if c == char:
      count = count + 1
  return count >= min and count <= max

def password_correct_position(pwd, char, positions):
  matches = 0
  for p in positions:
    if pwd[p-1] == char:
      matches = matches + 1
  return matches == 1

def test_password_correct_range():
  assert password_correct_range("asd", "w", 1, 3) == False
  assert password_correct_range("asd", "s", 1, 3) == True
  assert password_correct_range("asd", "w", 0, 3) == True
  assert password_correct_range("asdee", "e", 3, 3) == False
  assert password_correct_range("asdee", "e", 2, 2) == True
  assert password_correct_range("asd2e", "2", 1, 2) == True

def test_password_correct_position():
  assert password_correct_position("asd", "w", [1, 3]) == False
  assert password_correct_position("asds", "s", [2, 4]) == True
  assert password_correct_position("lllklx", "l", [1, 4]) == True
  
def test_answer():
  with open("./input.txt", "r") as input_file:
    passwords = list(map(lambda c: c.replace("\n", ""), input_file.readlines()))
    answer1 = 0
    answer2 = 0
    for p in passwords:
      matches = re.match(r'^(\d*)-(\d*)\s(\w):\s(.*)$', p, re.I)
      if password_correct_range(matches.group(4), matches.group(3), int(matches.group(1)), int(matches.group(2))):
        answer1 = answer1 + 1
      if password_correct_position(matches.group(4), matches.group(3), [int(matches.group(1)), int(matches.group(2))]):
        answer2 = answer2 + 1
    print("Answer1 is: {0}\n Answer2 is: {1}".format(answer1, answer2))

if __name__ == '__main__':
    test_answer()

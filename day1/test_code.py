import pytest
import itertools
import numpy

def find_which_sum(numbers_array, sum_amount):
  rtn = []
  for a in numbers_array:
    for b in numbers_array:
      if a + b == sum_amount:
        return [a,b]
  return rtn

def find_which_sum_extended(numbers_array, sum_amount, number_amount):
  possibilities = itertools.permutations(numbers_array, number_amount)
  for curr in possibilities:
    if numpy.sum(curr) == sum_amount:
      return curr


def test_find_which_sum():
  rtn = find_which_sum([2,3,4], 7)
  assert rtn == [3,4]

def test_answers():
  with open("./input.txt", "r") as input_file:
    test_numbers = list(map(lambda c: int(c.replace("\n", "")), input_file.readlines()))
    answer = find_which_sum(test_numbers, 2020)
    assert len(answer) == 2
    print(answer)
    answer = find_which_sum_extended(test_numbers, 2020, 3)
    assert len(answer) == 3
    print(answer)
  
if __name__ == '__main__':
    test_answers()
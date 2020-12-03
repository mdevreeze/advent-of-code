def test_answer():
  with open("./input.txt", "r") as input_file:
    landmap = list(map(lambda c: c.replace("\n", ""), input_file.readlines()))
    num_trees = 0
    i = 1
    for row in landmap:
        length = len(row)
        if row[i - 1] == "#":
            num_trees = num_trees + 1
        i = i + 3
        if i > length: 
            i = i - length

    print(num_trees)



if __name__ == '__main__':
    test_answer()
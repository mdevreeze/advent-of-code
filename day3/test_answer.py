def traverse(map, right=3, down=1):
    num_rows = len(map)
    num_trees = 0
    x = 1
    y = 0
    while y < num_rows:
        row = map[y]
        length = len(row)
        if row[x-1] == "#":
            num_trees = num_trees + 1
        x = x + right
        if x > length: 
            x = x - length
        y = y + down
    return num_trees

def test_answer():
  with open("./input.txt", "r") as input_file:
    landmap = list(map(lambda c: c.replace("\n", ""), input_file.readlines()))
    answer1 = traverse(landmap)
    print(answer1)
    print(traverse(landmap, 1, 1))
    print(traverse(landmap, 3, 1))
    print(traverse(landmap, 5, 1))
    print(traverse(landmap, 7, 1))
    print(traverse(landmap, 1, 2))

if __name__ == '__main__':
    test_answer()
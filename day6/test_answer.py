import itertools

def count_yes(group_votes):
    questions = itertools.chain(*group_votes)
    dic = index_voting(group_votes)
    all_yes = list(filter(lambda k: k in questions, dic.keys()))
    return len(all_yes)

def index_voting(group_votes):
    dic = {}
    for person_votes in group_votes:
        for vote in person_votes:
            if vote in dic:
                dic[vote] = dic[vote] + 1
            else:
                dic[vote] = 1
    return dic

def parse_text(input):
    data = []
    cur = []
    for line in input:
        if line:
            cur.append(line)
        else:
            data.append(cur) 
            cur = []
    if len(cur) > 0:
        data.append(cur) 
    return data

def test_unanimous_yesses():
    assert count_yes(["abc"]) == 3
    assert count_yes(["a", "b", "c"]) == 3
    assert count_yes(["ab", "ac"]) == 3
    assert count_yes(["a", "a", "a", "a"]) == 1
    assert count_yes(["b"]) == 1


def test_answer():
  with open("./input", "r") as input_file:
    input = list(map(lambda c: c.replace("\n", ""), input_file.readlines()))
    count = 0
    data = parse_text(input)
    for d in data:
        count = count + count_yes(d)
    print(count)


if __name__ == '__main__':
    test_answer()
import re
import pytest

def byr_valid(i):
    byr = int(i)
    return byr >= 1920 and byr <= 2002

def iyr_valid(i):
    iyr = int(i)
    return iyr >= 2010 and iyr <= 2020

def eyr_valid(i):
    iyr = int(i)
    return iyr >= 2020 and iyr <= 2030

def hgt_valid(i):
    if "cm" in i:
        cm = int(i.split("cm")[0])
        return cm >= 150 and cm <= 193
    if "in" in i:
        cm = int(i.split("in")[0])
        return cm >= 59 and cm <= 76
    return False

def hcl_valid(i):
    return re.match(r'\#[0-9a-f]{6}', i, re.IGNORECASE) != None

def ecl_valid(i):
    return i in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def pid_valid(i):
    return len(i) == 9 and int(i) > 0

def passport_validation(data):
    if not all (k in data for k in ("byr", "iyr", "eyr", "hgt" , "hcl", "ecl", "pid")):
        return False
    return (
        byr_valid(data["byr"]) 
        and iyr_valid(data["iyr"]) 
        and eyr_valid(data["eyr"]) 
        and hgt_valid(data["hgt"]) 
        and hcl_valid(data["hcl"]) 
        and ecl_valid(data["ecl"])
        and pid_valid(data["pid"])
    )

def parse_passport_lines(lines):
    data = {}
    for lines in lines:
        data_points = lines.split(" ")
        for point in data_points:
            splitted = point.split(":")
            key = splitted[0]
            value = splitted[1]
            data[key] = value 
    return data

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

def test_parse_lines():
    result = parse_passport_lines(["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", "byr:1937 iyr:2017 cid:147 hgt:183cm"])
    if "ecl" not in result or "cid" not in result:
        pytest.fail()
    if result["hcl"] != "#fffffd":
        pytest.fail()

def test_parse_text():
    result = parse_text([
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
        "",
        "hcl:#ae17e1 iyr:2013"
        "eyr:2024",
        "ecl:brn pid:760753108 byr:1931",
        "hgt:179cm",
    ])

    assert len(result) == 3


def test_invalid_passport_set():
    parsed = parse_text([
        "eyr:1972 cid:100",
        "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
        "",
        "iyr:2019",
        "hcl:#602927 eyr:1967 hgt:170cm",
        "ecl:grn pid:012533040 byr:1946",
        "",
        "hcl:dab227 iyr:2012",
        "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
        "",
        "hgt:59cm ecl:zzz",
        "eyr:2038 hcl:74454a iyr:2023",
        "pid:3556412378 byr:2007",
    ])
    for p in parsed:
        assert not passport_validation(parse_passport_lines(p))

def test_valid_passport_set():
    parsed = parse_text([
        "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
        "hcl:#623a2f",
        "",
        "eyr:2029 ecl:blu cid:129 byr:1989",
        "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
        "",
        "eyr:2029 ecl:blu cid:129 byr:1989",
        "hcl:#888785",
        "hgt:164cm byr:2001 iyr:2015 cid:88",
        "pid:545766238 ecl:hzl",
        "eyr:2022",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
    ])
    for p in parsed:
        assert passport_validation(parse_passport_lines(p))


def test_passport_validation_extended():
    assert byr_valid("2002")
    assert not byr_valid("2003")

    assert hgt_valid("60in")
    assert hgt_valid("190cm")
    assert not hgt_valid("190in")
    assert not hgt_valid("190")

    assert hcl_valid("#123abc")
    assert not hcl_valid("#123abz")
    assert not hcl_valid("123abc")

    assert ecl_valid("brn")
    assert not ecl_valid("wat")

    assert pid_valid("000000001")
    assert not pid_valid("0123456789")

def test_answer():
  with open("./input", "r") as input_file:
    input = list(map(lambda c: c.replace("\n", ""), input_file.readlines()))
    data = parse_text(input)
    valid = 0
    for p in data:
        passport_data = parse_passport_lines(p)
        if passport_validation(passport_data):
            valid = valid + 1
    print(valid)

if __name__ == '__main__':
    test_answer()
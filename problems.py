import math


print("==================== problem 1 ======================")


def get_distance(x1, y1, x2, y2):
    if isinstance(x1, int) & isinstance(x2, int) & isinstance(y1, int) & isinstance(y2, int):
        h_distance = float((x2 - x1) * 2)
        print(h_distance)
        y_distance = float((y2 - y1) * 2)
        print(y_distance)
        distance = math.sqrt(h_distance + y_distance)
        print(distance)
    else:
        print("not valid numbers")


get_distance(2, 2, 6, 8)

print("==================== problem 2 ======================")


def get_numbers(args):
    new_set = set(args)
    print(new_set)


get_numbers([1, 2, 2, 3, 2])

print("==================== problem 3 ======================")


def split_string(args):
    if len(args) % 2:
        part1 = args[0:int((len(args) / 2)) + 1]
        part2 = args[int((len(args) / 2)) + 1:int(len(args))]
        print(part1)
        print(part2)
    else:
        part1 = args[0:int((len(args) / 2))]
        part2 = args[int((len(args) / 2)):int(len(args))]
        print(part1)
        print(part2)


split_string("muhadaa")

print("==================== problem 4 ======================")

print('run "python3 prob4.py filename")
      
print("==================== problem 5 ======================")


def remove_vowel(args):
    vowel = ['a', 'o', 'u', 'e', 'i', ]
    for i in vowel:
        args = args.replace(i, '')
    print(args)


remove_vowel("muhammed")

print("==================== problem 6 ======================")


def get_index(args, ch):
    index = []
    for i in range(0, int(len(args))):
        if ch == args[i]:
            index.append(i)
    print(index)


get_index('youssef', 's')

with open('advent_day1') as file:
    total = file.readlines()


def part_one():
    count = 0
    for previous, current in zip(total[:-1], total[1:]):
        if int(previous) < int(current):
            count += 1
    print(count)


def part_two():
    count = 0
    for previous, current in zip(total, total[3:]):
        if int(previous) < int(current):
            count += 1
    print(count)


if __name__ == '__main__':
    part_one()
    part_two()

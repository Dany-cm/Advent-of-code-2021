with open('advent_day3', 'r') as file:
    total = file.read().splitlines()


def part_one():
    results = ''
    for line in range(len(total[0])):
        bitset = 0
        bitunset = 0
        for index in range(len(total)):
            if int(total[index][line]) & 1:
                bitset += 1
            else:
                bitunset += 1

        if bitset > bitunset:
            results += '1'
        else:
            results += '0'

    print(int(results, 2) * int(''.join('1' if x == '0' else '0' for x in results), 2))


if __name__ == '__main__':
    part_one()

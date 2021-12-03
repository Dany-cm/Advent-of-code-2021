with open('advent_day2') as file:
    total = file.readlines()


def part_one():
    forward = 0
    down = 0
    for word in total:
        data = word.split()
        match data[0]:
            case 'forward':
                forward += int(data[1])
            case 'down':
                down += int(data[1])
            case 'up':
                down -= int(data[1])
    result = forward * down
    print(f'Horizontal: {forward} Depth: {down} Results: {result}')


def part_two():
    forward = 0
    down = 0
    aim = 0

    for word in total:
        data = word.split()
        match data[0]:
            case 'forward':
                forward += int(data[1])
                down += aim * int(data[1])
            case 'down':
                aim += int(data[1])
            case 'up':
                aim -= int(data[1])
    result = forward * down
    print(f'Horizontal: {forward} Depth: {down} Results: {result}')


if __name__ == '__main__':
    part_one()
    part_two()

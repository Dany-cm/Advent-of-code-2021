with open('advent_day1') as file:
    total = file.readlines()

    count = 0
    for previous, current in zip(total[:-1], total[1:]):
        if int(previous) < int(current):
            count += 1
    print(count)

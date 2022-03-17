import math

for dataset in range(10):
    num_orange = 0
    num_blue = 0
    num_green = 0
    num_yellow = 0
    num_pink = 0
    num_violet = 0
    num_brown = 0
    num_red = 0

    done = False

    while not done:
        line = input()
        if line == 'end of box':
            done = True
        elif line == 'orange':
            num_orange = num_orange + 1
        elif line == 'blue':
            num_blue = num_blue + 1
        elif line == 'green':
            num_green = num_green + 1
        elif line == 'yellow':
            num_yellow = num_yellow + 1
        elif line == 'pink':
            num_pink = num_pink + 1
        elif line == 'violet':
            num_violet = num_violet + 1
        elif line == 'brown':
            num_brown = num_brown + 1
        elif line == 'red':
            num_red = num_red + 1

    handfuls = math.ceil(num_orange / 7) + math.ceil(num_blue / 7) + \
                math.ceil(num_green / 7) + math.ceil(num_yellow / 7) + \
                math.ceil(num_pink / 7) + math.ceil(num_violet / 7) + \
                math.ceil(num_brown / 7)

    print(handfuls * 13 + num_red * 16)

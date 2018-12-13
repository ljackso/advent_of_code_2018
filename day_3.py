#
# The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.
#
# Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and
# consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as
# follows:
#
# The number of inches between the left edge of the fabric and the left edge of the rectangle. The number of inches
# between the top edge of the fabric and the top edge of the rectangle. The width of the rectangle in inches. The
# height of the rectangle in inches. A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3
# inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the
# square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram
# below:
#
# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........
#
# The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For
# example, consider the following claims:
#
# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# Visually, these claim the following areas:
#
# ........ ...2222. ...2222. .11XX22. .11XX22. .111133. .111133. ........ The four square inches marked with X are
# claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)
#
# If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of
# fabric are within two or more claims?
#

# --- Part Two --- Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch
# of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make
# Santa's suit after all!
#
# For example, in the claims above, only claim 3 is intact after all claims are made.
#
# What is the ID of the only claim that doesn't overlap?


import numpy as np


def main():
    input_file = open('input/day_3_input.txt', 'r')
    fabric_ids = input_file.readlines()

    part_2(fabric_ids)


def part_2(fabric_ids):

    fabric_grid = np.array([[0] * 1000] * 1000)

    for fabric_id in fabric_ids:

        instructions = parse_fabric_id(fabric_id)

        start_x = instructions[0][0]
        start_y = instructions[0][1]
        size_x = instructions[1][0]
        size_y = instructions[1][1]

        for i in range(0, size_y):
            for j in range(0, size_x):
                fabric_grid[start_y + i][start_x + j] += 1

    for fabric_id in fabric_ids:

        instructions = parse_fabric_id(fabric_id)

        start_x = instructions[0][0]
        start_y = instructions[0][1]
        size_x = instructions[1][0]
        size_y = instructions[1][1]

        overlaps = 0
        for i in range(0, size_y):
            for j in range(0, size_x):
                overlaps += (1 if fabric_grid[start_y + i][start_x + j] > 1 else 0)

        if overlaps == 0:
            print(fabric_id)




def part_1(fabric_ids):
    fabric_grid = np.array([[0] * 1000] * 10000)
    print(fabric_grid)

    for fabric_id in fabric_ids:

        instructions = parse_fabric_id(fabric_id)

        start_x = instructions[0][0]
        start_y = instructions[0][1]
        size_x = instructions[1][0]
        size_y = instructions[1][1]

        for i in range(0, size_y):
            for j in range(0, size_x):
                fabric_grid[start_y + i][start_x + j] += 1

    count_clash = 0
    for row in fabric_grid:
        for item in row:
            count_clash += (1 if item > 1 else 0)

    print(str(count_clash) + ' clashes')


def parse_fabric_id(id):
    trimmed = id.replace(' ', '')

    start_point = [int(x) for x in trimmed.split('@')[1].split(':')[0].split(',')]
    dimensions = [int(x) for x in trimmed.split('@')[1].split(':')[1].split('x')]

    return start_point, dimensions


if __name__ == "__main__":
    main()

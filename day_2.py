
#
# To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID
# containing exactly two of any letter and then separately counting those with exactly three of any letter. You can
# multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.
#
# For example, if you see the following box IDs:
#
# abcdef contains no letters that appear exactly two or three times.
# bababc contains two a and three b, so it counts for both.
# abbcde contains two b, but no letter appears exactly three times.
# abcccd contains three c, but no letter appears exactly two times.
# aabcdd contains two a and two d, but it only counts once.
# abcdee contains two e.
# ababab contains three a and three b, but it only counts once.
#
# Of these box IDs, four of them contain a letter which
# appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these
# together produces a checksum of 4 * 3 = 12.
#
# What is the checksum for your list of box IDs?
#
# --- Part Two ---
# Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.
#
# The boxes will have IDs which differ by exactly one character at the same position in both strings. For example,
# given the following box IDs:
#
# abcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz

# The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However,
# the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.
#
# What letters are common between the two correct box IDs? (In the example above, this is found by removing the
# differing character from either ID, producing fgij.)


def main():
    input_file = open('input/day_2_input.txt', 'r')
    box_ids = input_file.readlines()

    part_2(box_ids)


def part_2(box_ids):
    for i in range(0, len(box_ids)):
        for j in range(i + 1, len(box_ids)):
            index = check_match(box_ids[i][:-1], box_ids[j][:-1])
            if index != -1:
                id = box_ids[i][:-1]
                print(box_ids[i][:-1] + ' line ' + str(i))
                print(box_ids[j][:-1] + ' line ' + str(j))
                print(id[:index] + id[index+1:])
                print('QED')


def part_1(box_ids):
    double_count = 0
    triple_count = 0
    for box_id in box_ids:
        #use [:-1] to remove new line character from string when parsing
        double_count += (1 if contains_duplicates(box_id[:-1], 2) else 0)
        triple_count += (1 if contains_duplicates(box_id[:-1], 3) else 0)

    print(double_count)
    print(triple_count)
    print(double_count * triple_count)


def contains_duplicates(str_id, amount):

    count = {}
    for letter in str_id:
        if letter in count.keys():
            count[letter] += 1
        else:
            count[letter] = 1

    matches = 0
    for key in count:
        if count[key] == amount:
            matches += 1

    return matches > 0

def check_match(str_id_1, str_id_2):

    match_checker = [False] * len(str_id_1)

    for i in range(0, len(str_id_1)):
        match_checker[i] = (str_id_1[i] == str_id_2[i])

    count_false_index = -1
    count_false = 0
    for i in range(0, len(match_checker)):
        count_false += (1 if not match_checker[i] else 0)
        if match_checker[i] == False:
            count_false_index = i

    if count_false == 1:
        return count_false_index

    return -1


if __name__ == "__main__":
    main()

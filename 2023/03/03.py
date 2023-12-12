def gear_ratios_first_puzzle(input) -> int:
    output = 0

    for i, line in enumerate(input):
        current_num = 0
        symbol_present = False

        for j, char in enumerate(line):
            if char.isdigit():
                if not line[j - 1].isdigit():
                    current_num = int(char)
                else:
                    current_num = (current_num * 10) + int(char)

                # Check for symbol around digit
                for ii in [i - 1, i, i + 1]:
                    for jj in [j - 1, j, j + 1]:
                        if 0 <= ii < len(input) and 0 <= jj < len(line):
                            if not input[ii][jj].isdigit() and input[ii][jj] != '.':
                                symbol_present = True

                # Check if num has ended
                if j == len(line) - 1 or not line[j + 1].isdigit():
                    if symbol_present:
                        output += current_num
                        symbol_present = False
                        current_num = 0

    return output


def gear_ratios_second_puzzle(input) -> int:
    output = 0
    nums_with_stars = {}

    for i, line in enumerate(input):
        symbol_present = False
        symbol_positions = (-1, -1)

        for j, char in enumerate(line):
            if char.isdigit():
                if not line[j - 1].isdigit():
                    current_num = int(char)
                else:
                    current_num = (current_num * 10) + int(char)

                # Check for symbol around digit
                for ii in [i - 1, i, i + 1]:
                    for jj in [j - 1, j, j + 1]:
                        if 0 <= ii < len(input) and 0 <= jj < len(line):
                            if not input[ii][jj].isdigit() and input[ii][jj] != '.':
                                symbol_present = True
                                symbol_positions = (ii, jj)

                # Check if num has ended
                if j == len(line) - 1 or not line[j + 1].isdigit():
                    if symbol_present and current_num > 0:
                        if symbol_positions in nums_with_stars:
                            nums_with_stars[symbol_positions].append(current_num)
                        else:
                            nums_with_stars[symbol_positions] = [current_num]

                        symbol_present = False
                        symbol_positions = (-1, -1)
                        current_num = 0

    for symbol_positions in nums_with_stars:
        if len(nums_with_stars[symbol_positions]) == 2:
            first_num = nums_with_stars[symbol_positions][0]
            second_num = nums_with_stars[symbol_positions][1]
            output += first_num * second_num

    return output


with open("input.txt", 'r') as f:
    input = f.read().splitlines()

print(f"First: {gear_ratios_first_puzzle(input)}")
print(f"Second: {gear_ratios_second_puzzle(input)}")

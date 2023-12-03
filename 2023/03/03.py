def gear_ratios_first_puzzle(input) -> int:
    output = 0

    for line in input:
        if input.index(line) == 0:
            nextLine = input[line+1]
            for char in line:
                if line.index(char) == 0:
                    if char.isdigit():
                        pass
        elif input.index(line) == len(line):
            pass
        else:
            pass

    return output


def gear_ratios_second_puzzle(input) -> int:
    pass


with open("input.txt") as f:
    input = f.read().splitlines()

print(f"First: {gear_ratios_first_puzzle(input)}")
# print(f"Second: {gear_ratios_second_puzzle(input)}")

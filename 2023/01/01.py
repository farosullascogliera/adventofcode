def trebuchet_first_part(input) -> int:
    output = 0

    for line in input:
        numbers = [0] * 2
        first_encounter = True
        for char in line:
            if char.isdigit():
                if first_encounter:
                    numbers = [int(char), int(char)]
                    first_encounter = False
                else:
                    numbers[1] = int(char)
        output += (numbers[0] * 10) + numbers[1]

    return output


def trebuchet_second_part(input) -> int:
    output = 0

    for line in input:
        first_encounter = True
        numbers = [0] * 2
        substring = ""

        for char in line:
            if char.isdigit():
                if first_encounter:
                    numbers = [int(char), int(char)]
                    first_encounter = False
                else:
                    numbers[1] = int(char)
                substring = ""
            else:
                substring += char
                numFound = findNumber(substring)
                if numFound != 0:
                    if first_encounter:
                        numbers = [numFound, numFound]
                        first_encounter = False
                        substring = substring[-1]
                    else:
                        numbers[1] = numFound
                        substring = substring[-1]

        output += (numbers[0] * 10) + numbers[1]

    return output


def findNumber(s) -> int:
    if "one" in s:
        n = 1
    elif "two" in s:
        n = 2
    elif "three" in s:
        n = 3
    elif "four" in s:
        n = 4
    elif "five" in s:
        n = 5
    elif "six" in s:
        n = 6
    elif "seven" in s:
        n = 7
    elif "eight" in s:
        n = 8
    elif "nine" in s:
        n = 9
    else:
        n = 0

    return n


with open("input.txt") as f:
    input = f.read().splitlines()

print(f"First part: {trebuchet_first_part(input)}")
print(f"Second part: {trebuchet_second_part(input)}")

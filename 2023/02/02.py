def cube_conundrum_first_part(input) -> int:
    output = 0
    # maxCubes 12R, 13G, 14B

    for line in input:
        outmaxed = False
        gameID = int(line.split(': ')[0][5:])
        sets = line.split(': ')[1].replace(';', ',').split(', ')

        for cubes in sets:
            number = int(cubes.split(' ')[0])
            if number > 14:
                outmaxed = True
                break

            color = cubes.split(' ')[1]
            if ((color == "red" and number > 12) or
                    (color == "green" and number > 13) or
                    (color == "blue" and number > 14)):
                outmaxed = True
                break

        if not outmaxed:
            output += gameID

    return output


def cube_conundrum_second_part(input) -> int:
    output = 0
    powerMinimum = 0

    for line in input:
        minCubes = [0] * 3
        sets = line.split(': ')[1].replace(';', ',').split(', ')

        for cubes in sets:
            number = int(cubes.split(' ')[0])
            color = cubes.split(' ')[1]

            if color == "red" and number > minCubes[0]:
                minCubes[0] = number
            if color == "green" and number > minCubes[1]:
                minCubes[1] = number
            if color == "blue" and number > minCubes[2]:
                minCubes[2] = number

        powerMinimum = minCubes[0] * minCubes[1] * minCubes[2]
        output += powerMinimum

    return output


with open("input") as f:
    input = f.read().splitlines()

print(f"First part: {cube_conundrum_first_part(input)}")
print(f"Second part: {cube_conundrum_second_part(input)}")

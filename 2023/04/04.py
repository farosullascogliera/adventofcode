def scratchcards_first(input) -> int:
    output = 0

    for line in input:
        winning_numbers = {}
        matches = line.split(' | ')
        first_match = matches[0].split(':')
        first_match = first_match[1].split(' ')
        second_match = matches[1].split(' ')

        for number in first_match:
            if number != '':
                winning_numbers[int(number)] = False

        for number in second_match:
            if number != '':
                number = int(number)
                if number in winning_numbers:
                    winning_numbers[number] = True

        points = 0
        for number in winning_numbers:
            if winning_numbers[number]:
                if points == 0:
                    points += 1
                else:
                    points *= 2

        output += points

    return output


def scratchcards_second(input) -> int:
    output = 0
    cards_instances = {}

    for i, line in enumerate(input):
        cards_instances[i + 1] = 1

    for i, line in enumerate(input):
        matches = line.split(' | ')
        first_match = matches[0].split(':')
        first_match = first_match[1].split(' ')
        second_match = matches[1].split(' ')

        for j in range(cards_instances[i + 1]):
            winning_numbers = {}

            for number in first_match:
                if number != '':
                    winning_numbers[int(number)] = False

            for number in second_match:
                if number != '':
                    number = int(number)
                    if number in winning_numbers:
                        winning_numbers[number] = True

            points = 0
            for number in winning_numbers:
                if winning_numbers[number]:
                    points += 1

            for point in range(points):
                cards_instances[point + 2 + i] += 1

    for cards in cards_instances:
        output += cards_instances[cards]

    return output


with open("input.txt", 'r') as f:
    input = f.read().splitlines()

print(f"First: {scratchcards_first(input)}")
print(f"Second: {scratchcards_second(input)}")

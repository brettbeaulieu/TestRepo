import random


def diceRoll():
    total_rolls = 2
    result = []

    for roll in range(total_rolls):
        result.append(random.randint(1, 6))

    rolls_sum = sum(result)

    print(f'Rolls: {result}')
    print(f'Sum: {rolls_sum}')
    print(f'Average: {rolls_sum / total_rolls}')


if __name__ == "__main__":
    diceRoll()

import random

# Task 19
def twoDiceRoll():
    total_rolls = 2
    result = []

    for roll in range(total_rolls):
        result.append(random.randint(1, 6))

    rolls_sum = sum(result)
    print("Two Dice Roll Summary: ")
    print(f'Rolls: {result}')
    print(f'Sum: {rolls_sum}')
    print(f'Average: {rolls_sum / total_rolls}')


if __name__ == "__main__":
    twoDiceRoll()

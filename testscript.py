import random

# Task 19
def twoDiceRoll():
    total_rolls = 2
    result = []
    # a new comment
    #SBT-34 stuff
    # mostly important -- SBT-52
    for roll in range(total_rolls):
        result.append(random.randint(1, 6))

    print("Testing for SBT-18")
    rolls_sum = sum(result)
    print("Testing for SBT-17 (No Caps)")
    print("Two Dice Roll Summary: ")
    print(f'Rolls: {result}')
    print(f'Sum: {rolls_sum}')
    print(f'Average: {rolls_sum / total_rolls}')


if __name__ == "__main__":
    twoDiceRoll()

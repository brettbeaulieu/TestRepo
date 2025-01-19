import random


def main():
    total_rolls = 2
    result = []

    for roll in range(total_rolls):
        result.append(random.randint(1, 6))

    print(sum(result))


if __name__ == "__main__":
    main()

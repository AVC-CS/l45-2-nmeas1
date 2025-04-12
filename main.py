import random


def main():
    total = 0
    numbers = []

    while total < 100:
        randnum = random.randint(1,10)
        if total + randnum > 100:
            break
        total += randnum
        numbers.append(randnum)

    

    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()

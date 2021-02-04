from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    i = 2
    top = sqrt(x)
    while i <= top:
        if x % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
    with open('2006_output.txt', mode='w+', encoding='utf-8') as f:
        for i in range(100, 1001):
            if '9' not in str(i) and is_prime(i):
                f.write(str(i) + '\n')
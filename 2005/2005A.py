# 将一个数拆成多个素数之和


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


res = []


def split_prime(num):
    if num < 2:
        return
    if is_prime(num):
        res.append(num)
        return

    for i in range(num, 1, -1):
        if is_prime(i) and num-i >= 2:
            res.append(i)
            split_prime(num-i)
            return


if __name__ == '__main__':
    while True:
        num = int(input())
        split_prime(num)
        print(str(res))
        res.clear()

from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    top = sqrt(x)
    i = 2
    while i <= top:
        if x % i == 0:
            return False
        i += 1
    return True


def reverse_num(num):
    return int(str(num)[::-1])


def judge(num):
    return is_prime(num) and is_prime(reverse_num(num))


def filter_prime(start, end):
    res = [i for i in range(start, end + 1) if judge(i)]
    return res


def save2file(filename, text):
    with open(filename, mode='w+', encoding='utf-8') as f:
        f.write(text)


def main():
    res = filter_prime(10, 1000)
    print(res)
    save2file('2007B_output.txt', str(res))


if __name__ == '__main__':
    main()
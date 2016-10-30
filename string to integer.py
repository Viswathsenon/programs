def main():
    s = str(input("Enter the string  "))
    f = conversion(s)
    print("The string and the integer are %s and %d"%(s, f))


def conversion(x):
    power = a = 0
    for i in reversed(x):
        a += (ord(i) - 48) * 10 ** power
        power = power + 1
    return a


if __name__ == '__main__':
    main()
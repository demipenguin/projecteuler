def p9():
    for a in range(1, 1000):
        for b in range(1, a):
            c = 1000 - a - b
            if a ** 2 + b ** 2 + c ** 2 == 2 * max(max(a, b), c) ** 2:
                print a * b * c
                return

if __name__ == '__main__':
    p9()
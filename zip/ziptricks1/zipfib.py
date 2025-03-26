

def fibber(f0=0, f1=1, n=-1):
    while n !=0:
        n -= 1
        yield f0
        f0, f1 = f1, f0 + f1

def main():
    # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
    for i, fib in zip(range(20), fibber()): # f0, f1 in zip(range(20), gFO(), gF1()):
        print(f"{i}: {fib}")

    for i, fib in enumerate(fibber(n=20)):
        print(f"{i}: {fib}")

    for fib in fibber(n=20):
        print(fib)



    return

if __name__ == '__main__':
    main()
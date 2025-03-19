
def lzip(*args):
    return list(zip(*args))

def main():

    a1 = [0,1,2,3,4]
    a2 = ['a', 'b', 'c', 'd', 'e']
    a3 = [ 'A', 'B', 'C', 'D', 'E']

    a1a = lzip(a1, a2, a3)
    a1b = lzip([a1, a2, a3])

    return

if __name__ == '__main__':
    main()
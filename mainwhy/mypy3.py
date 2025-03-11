
def MyFunc(a,b):
    return a+b

#
# test MyFunc (testing is good!)
#
def main():
    assert MyFunc(2,2) == 4
    print(f"success!  ({__name__})")

if __name__ == '__main__':
    main()
    

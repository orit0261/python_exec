from collections import Counter

if __name__ == '__main__':
    lst=[1,2,3,4]
    print(sum(lst))
    print(len(lst))
    print(sum(lst))

    n = int(input())
    arr = Counter(map(int, input().split())).keys()

    arr = list(set(map(int, input().split())))
    arr.sort()
    print(arr[-2])


n = input()
set1 = set(map(int, input().split()))
com_=input()
for i in range(int(com_)):
    x=input()
    x = x.split(' ')
    print(x)
    if x[0] =='pop':
        set1.pop()
    elif x[0]=='remove':
        set1.remove(int(x[1]))
    else:
        if x[0]=='discard':
          set1.discard(int(x[1]))

print(sum(set1))
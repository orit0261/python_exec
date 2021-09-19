if __name__ == '__main__':
    arr = []
    for i in range(int(input())):
        s = input().split()
        for i in range(1, len(s)):
            s[i] = int(s[i])
            if s[0]=='append':
             arr.append(str(s[1]))
            else:
             if s[0] == 'insert':
               arr.insert(int(s[2]),str(s[1]))
             else:
                if s[0] == 'remove':
                    arr.remove(str(s[1]))
                else:
                   if s[0] == 'sort':
                       arr.sort()
                   else:
                     if s[0] == 'pop':
                         arr.pop()
                     else:
                         if s[0] == 'reverse':
                             arr.reverse()

    print(arr)





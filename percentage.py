dict_scors={}
for i in range(int(input())):
    name = input()
    score = list(map(int,input().split()))
    dict_scors[name]=score

find_name = input()
print('{0:.2f}'.format(sum(dict_scors[find_name])/len(dict_scors[find_name])))



def sort_second():
    dict_scors={}
    for i in range(int(input())):
        name = input()
        score = float(input())
        if score in dict_scors:
            dict_scors[score].append(name)
        else:
            dict_scors[score] = [name]

    new_list=[]
    for i in dict_scors:
            new_list.append([i,dict_scors[i]])
    new_list.sort()
    result = new_list[1][1]
    result.sort()
    print(*result, sep="\n")

sort_second()



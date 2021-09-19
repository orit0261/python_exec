# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    lst = [2,1,0,4,7]
    lst.insert(2,999)
    lst.append(4)
    print(lst)
    lst.sort()
    print(lst)

    lst.pop()
    print(lst)
    lst.reverse()
    print(lst)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
#    lst_names=[]
#    lst_grades=[]
#    for _ in range(int(input())):
#        name = input()
#        score = float(input())
#        lst_names.append(name)
#        lst_grades.append(score)

#    lst_names.sort()
#    print("sorted names:", lst_names)
#    lst_grades.sort()
#    lst_grades.reverse()
#    print("Second largest element is:", lst_grades[-2])


    score_list = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in score_list:
            score_list[score].append(name)
        else:
            score_list[score] = [name]

    new_list = []
    for i in score_list:
        new_list.append([i, score_list[i]])

    print(new_list)
    new_list.sort()
    result = new_list[1][1]
    result.sort()
    print(*result, sep="\n")

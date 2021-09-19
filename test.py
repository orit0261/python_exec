def calc(sum):
    arr1 = [1, 2, 3, 5]
    for i in range(len(arr1)):
        if i+1<len(arr1):
          if arr1[i]+arr1[i+1]==sum:
            return True
    return False

if __name__ == '__main__':
    sum=5
    print(calc(sum))

from linearSearch import linear_search

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
m = 3
value = 12


def jump_search(arr, n, m, value):

    jump = 0
    tmp = []
    flag = 1

    for i in range(0, n, m):
        #print("i: " + str(i))
        jump += 1
        if (arr[i] == value):
            flag = 0
            break
        else:
            if (arr[i] >= value):
                for j in range(i-m-1, i-m+1):
                    tmp.append(arr[j])
                #print("INNER: ")
                #print(tmp)
                steps = linear_search(tmp, len(tmp), value)
                jump += steps
                flag = 0
                break
    if(flag):
        for j in range(n-m+1, n):
            tmp.append(arr[j])
            #print("OUTER:")
            #print(tmp)
        steps = linear_search(tmp, len(tmp), value)
        jump += steps

    return jump


print(jump_search(arr, len(arr), m, value))

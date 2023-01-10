from linearSearch import linear_search

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = 3
value = 20


def jump_search(arr, n, m, value):

    jump = 0
    tmp = []
    flag = 1
    max = 0

    if (n == 0):
        return jump

    for i in range(0, n, m):
        print("i: " + str(i))
        jump += 1
        max = i
        if (arr[i] == value):
            flag = 0
            break
        else:
            if (arr[i] >= value):
                for j in range(i-m+1, i):
                    tmp.append(arr[j])
                #print("INNER: ")
                # print(tmp)
                steps = linear_search(tmp, len(tmp), value)
                jump += steps
                flag = 0

                break
    if(flag):
        # print(max)
        for j in range(max+1, n):
            tmp.append(arr[j])
            print("OUTER:")
            print(tmp)
        steps = linear_search(tmp, len(tmp), value)
        jump += steps

    return jump


print(jump_search(arr, len(arr), m, value))

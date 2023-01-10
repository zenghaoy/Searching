arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def linear_search(arr, length, value):

    steps = 0

    for i in range(0, length):
        steps += 1
        if arr[i] == value:
            print("Found value: "+str(value))
            break
    return steps


#print(linear_search(arr, len(arr), 10))

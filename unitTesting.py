import jumpSearch


def test_cases():

    # empty array
    arr = []
    m = 3
    value = 20
    result = 0
    assert jumpSearch.jump_search(arr, len(arr), m, value) == 0

    # result does exist
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = 3
    value = 10
    assert jumpSearch.jump_search(arr, len(arr), m, value) == 4

    # result does exist at the front
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    m = 3
    value = 2
    assert jumpSearch.jump_search(arr, len(arr), m, value) == 3

    # result does exist at the front
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    m = 3
    value = 3
    assert jumpSearch.jump_search(arr, len(arr), m, value) == 4

    # result does exist in the middle
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    m = 3
    value = 6
    assert jumpSearch.jump_search(arr, len(arr), m, value) == 5

    # result does exist at the end
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    m = 3
    value = 12
    assert jumpSearch.jump_search(arr, len(arr), m, value) == 6

    # result does not exist
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = 3
    value = 12
    assert jumpSearch.jump_search(
        arr, len(arr), m, value) <= (len(arr)/m + (m-1))

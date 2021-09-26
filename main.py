def get_permutations(arr):
    # Write your code here

    if len(arr) == 0:
        return []

    i = 0
    l = len(arr) - 1
    res = []

    helper(arr, [], res)
    print(res)
    return res


def helper(arr, slate, res):
    if len(arr) == 0:
        return res.append(slate.copy())
    else:
        for i in range(len(arr)):
            slate.append(arr[i])
            helper(arr[:i]+arr[i+1:len(arr)], slate, res)
            slate.pop()

    return res

if __name__ == '__main__':
    arr = [1, 2, 2]
    get_permutations(arr)
    # curr = arr[len(s)]
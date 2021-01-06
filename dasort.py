def sorter(arr):
    lo, min_to_move, mtm_k, to_move = (1000000001, 1000000001, len(arr), set())

    for k, v in enumerate(reversed(arr)):
        if v > lo:
            to_move.add(len(arr) - 1 - k)
            if v <= min_to_move:
                min_to_move = v
                mtm_k = len(arr) - 1 - k
        else:
            lo = v

    if arr[-1] == min_to_move:
        return len(to_move)

    for k, v in enumerate(arr[mtm_k + 1:]):
        if v > min_to_move:
            to_move.add(mtm_k + 1 + k)
    return len(to_move)


for i in range(int(input())):
    arr_num, arr_len = map(int, input().split())
    lis = []
    for arr_num in range(arr_len // 10 + (1 if arr_len % 10 > 0 else 0)):
        lis.extend(map(int, input().split()))
    num_deletes = sorter(lis)
    print('{} {}'.format(i + 1, num_deletes))

def solution(heights, length):
    stack = list()
    block_count = 0

    for H in heights:

        while len(stack) and stack[-1] > H:
            stack.pop()

        if len(stack) and stack[-1] == H:
            continue
        else:
            stack.append(H)
            block_count += 1

    return block_count


if __name__ == '__main__':
    from random import randint

    count = solution(heights=[8, 8, 5, 7, 9, 8, 7, 4, 8], length=9)
    print('Block count is {0}'.format(count))

    N = randint(1, 1000000)
    H = [randint(1, 1000000000) for _ in range(100000)]

    count = solution(H, N)
    print('Block count is {0}'.format(count))


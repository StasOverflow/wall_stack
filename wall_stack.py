def solution(heights, length):
    stack = list()
    block_count = 0

    for H in heights:

        if len(stack) and stack[-1] > H:
            stack.pop()
        elif len(stack) and stack[-1] == H:
            continue

        if not(len(stack)) or stack[-1] < H:
            stack.append(H)
            block_count += 1

        print('H is {0}, stack is {1}'.format(H, stack))

    return block_count


if __name__ == '__main__':
    count = solution(heights=[8, 8, 5, 7, 9, 8, 7, 4, 8], length=9)
    print('Block count is {0}'.format(count))

def ur(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5

    if remainder-small > 0:
        print(-1)
    else:
        print(remainder)

ur(2, 3, 17)
ur(9, 1, 14)

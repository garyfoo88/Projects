def message(abc, n):
    for i in abc[:-1]:
        for d in abc[1:]:
            if (d + i) == n:
                return True


print(message([1, 2, 3, 4, 5], 7))

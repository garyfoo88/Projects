def message(abc):
    cde = []

    for i in abc:
        c = 1
        count = 0
        for v in abc:
            c = c * v
        while c > 0:
            c -= i
            count += 1

        cde.append(count)

    return cde


print(message([1, 2, 3, 4, 5]))

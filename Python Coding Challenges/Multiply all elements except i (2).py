def message(abc):
    cde = []
    d = abc[:]
    z = abc
    x = len(d)
    c = 1
    for i in range(x):

        z.pop(i)

        for b in z:
            c = c * b

        cde.append(c)
        z.insert(i, d[i])
        c = 1
    return cde


print(message([3, 2, 1]))


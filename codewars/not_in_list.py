def array_diff(a, b):
    liste = []
    for i in a:
        if i in b:
            pass
        else:
            liste.append(i)
    return liste

print(array_diff([1,3, 3, 3, 2], [ 3]))
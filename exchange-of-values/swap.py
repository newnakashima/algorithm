def swap(x, y):
    temp = x
    x = y
    y = temp
    return (x, y)

a, b = 3, 2
print("Before: a = %d, b = %d" % (a, b))
a, b = swap(a, b)
print("After: a = %d, b = %d" % (a, b))

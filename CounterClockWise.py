def CounterClockwise(a):
    m = []
    n = []
    size = len(a)
    for col in range(size):
        inner = []
        for row in range(len(a)):
            inner.append(a[row][col])
        m.append(inner)
    n = (m[2],m[1],m[0])
    return n

list_awal = [[1,2,3],
            [4,5,6],
            [7,8,9]]
print(CounterClockwise(list_awal))
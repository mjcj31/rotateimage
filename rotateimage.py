# coding challenge from codesignal
# image rotation simulation using a 2d array

def rotateImage(a):
    global j
    global temp
    print(a)
    for i in range(len(a) // 2):
        end = len(a) - 1 - i
        for j in range(end - i):
            temp = a[i][i + j]
            a[i][i + j] = a[end - j][i]
            a[end - j][i] = a[end][end - j]
            a[end][end - j] = a[i + j][end]
            a[i + j][end] = temp
    print(a)


# rotateImage([[1,2,3],
            # [4,5,6],
            # [7,8,9]])
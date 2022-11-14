arr_2d = [[1,2,3],
       [4,5,6],
       [7,8,9]]

def print_matrix(arr):
    for i in range(len(arr)):
        for a in range(len(arr[i])):
            print(arr[i][a], end=' ')
        print()


def create_2d_arr(m,n):
    arr_2d = []

    for i in range(m):
        internal_arr = []

        for j in range(n):
            internal_arr.append(0)

        arr_2d.append(internal_arr)

    return arr_2d

q = create_2d_arr(5,10)

#print_matrix(q)

'''
       [1,2,3]
       [4,5,6]
       [7,8,9]
'''

def swap(aa, n, j):
    temp = aa[n]
    aa[n] = aa[j]
    aa[j] = temp

def mirror_2d_arr(arr_2d):
    for aa in arr_2d:
        for i in range(len(aa) // 2):
            print(i)
            aa[i], aa[-i -1] = aa[-i -1], aa[i]
            print('q ' + str(aa[i]))
            print('w ' + str(aa[-i -1]))
            #swap(aa, i, len(aa) - 1 - i)

mirror_2d_arr(arr_2d)
print_matrix(arr_2d)







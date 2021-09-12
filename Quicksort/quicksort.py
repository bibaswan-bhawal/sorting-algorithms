array = [3,8,2,5,1,4,7,6]

def partition_subroutine(array, p):
    if p != 0:
        tmp = array[0]
        array[0] = array[p]
        array[p] = tmp

    i = 1

    for j in range(1,len(array)):
        if array[j] < array[0]:
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
            i += 1
            
    tmp = array[i-1]
    array[i-1] = array[0]
    array[0] = tmp

    return array, i


def quicksort(array, length):
    array, i = partition_subroutine(array, 0)


    

quicksort(array, len(array))
import random
import math
numbers = []
sorted_numbers = []


def generate_numbers(length, min, max):
    for i in range(0, length):
        numbers.append(random.randint(min, max))
    print(numbers)
    return numbers


def sort(unsorted):
    first_half = unsorted[0:math.ceil(len(unsorted)/2)]
    second_half = unsorted[math.ceil(len(unsorted)/2):]
    if len(unsorted) > 2:
        first_half_sorted = sort(first_half)
        second_half_sorted = sort(second_half)
    else:
        first_half_sorted = first_half
        second_half_sorted = second_half
        
    sorted_half = []
    i = 0
    j = 0

    for k in range(0, len(first_half_sorted) + len(second_half_sorted)):
        if i >= len(first_half_sorted):
            for item in second_half_sorted[j:]:
                sorted_half.append(item)
            break
        if j >= len(second_half_sorted):
            for item in first_half_sorted[i:]:
                sorted_half.append(item)
            break

        if first_half_sorted[i] < second_half_sorted[j]:
            sorted_half.append(first_half_sorted[i])
            i += 1
        else:
            sorted_half.append(second_half_sorted[j])
            j += 1

    return sorted_half


print(sort(generate_numbers(100, 0, 1000)))

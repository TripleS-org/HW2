"""Module providing the function of MergeSort"""
import rand


def merge_sort(arr):
    """Function implementing sorting algorithm."""
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """Function that returns merged array"""
    left_index = 0
    right_index = 0
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    while left_index < len(left_arr):
        merge_arr.append(left_arr[left_index])
        left_index += 1

    while right_index < len(right_arr):
        merge_arr.append(right_arr[right_index])
        right_index += 1

    return merge_arr


input_arr = rand.random_array([None] * 20)
sorted_arr = merge_sort(input_arr)

print(sorted_arr)

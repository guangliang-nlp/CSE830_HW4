from __future__ import division
import copy
import time
import random
import matplotlib.pyplot as plt


# source https://coderslegacy.com/python/merge-sort-algorithm/
def mergeSort(x, k):
    if len(x) < 2:  # Return if array was reduced to size 1
        return x

    result = []  # Array in which sorted values will be inserted
    mid = int(len(x) / 2)
    if mid <= k:
        y = insertionSort(x[:mid])
        z = insertionSort(x[mid:])
    else:
        y = mergeSort(x[:mid], k)  # 1st half of array
        z = mergeSort(x[mid:], k)  # 2nd half of array
    i = 0
    j = 0
    while i < len(y) and j < len(z):  # Stop if either half reaches its end
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]  # Add left over elements
    result += z[j:]  # Add left over elements
    return result


# source: https://www.programiz.com/dsa/insertion-sort
def insertionSort(input_arr):
    # We start from 1 since the first element is trivially sorted
    array = copy.deepcopy(input_arr)
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert - move
        # that element to the right
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition - 1]
            currentPosition = currentPosition - 1

        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        array[currentPosition] = currentValue
    return array


def load_sample_input(file):
    sample_input = []
    for line in open(file):
        sample_input.append(float(line.strip()))
    return sample_input


def get_run_time_merge(input_arr, k):
    time_start = time.time()
    run_iters = 100
    for i in range(run_iters):
        array = copy.deepcopy(input_arr)
        mergeSort(array, k)
    time_end = time.time()
    run_time_merge = time_end - time_start
    return run_time_merge / run_iters


def get_run_time_insert(input_arr):
    time_start_ = time.time()
    run_iters = 100
    for i in range(run_iters):
        array = copy.deepcopy(input_arr)
        insertionSort(array)
    time_end_ = time.time()
    run_time_insert = time_end_ - time_start_
    return run_time_insert / run_iters


input = load_sample_input("sample_input")

"""
    cal the run time of merge sort with/-out modified recursion step
    with input n = 200,300,500 and k=66
"""
# n = 200

for n in [10, 50, 100, 150, 200, 250]:
    input_k_list = []
    run_time_merge_modify_list, run_time_merge_list, run_time_insert_list = [], [], []

    for k in range(2, n, 1):
        print(k)
        input_k_list.append(k)
        run_time_merge_ = get_run_time_merge(input[:n], k=k)
        run_time_merge = get_run_time_merge(input[:n], k=-1)
        run_time_insert = get_run_time_insert(input[:n])

        run_time_merge_modify_list.append(run_time_merge_)
        run_time_merge_list.append(run_time_merge)
        run_time_insert_list.append(run_time_insert)

    plt.plot(input_k_list, run_time_merge_modify_list, color="r", label="merge_sort_modify")
    plt.plot(input_k_list, run_time_merge_list, color="g", label="merge_sort")
    plt.plot(input_k_list, run_time_insert_list, color="b", label="insertion_sort")
    plt.title("input size n={0}".format(n))
    plt.xlabel("k")
    plt.ylabel("run time")
    plt.legend()
    plt.show()

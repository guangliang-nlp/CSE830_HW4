from __future__ import division

import copy
import random
import time
import matplotlib.pyplot as plt


# source https://coderslegacy.com/python/merge-sort-algorithm/
def mergeSort(x):
    if len(x) < 2:  # Return if array was reduced to size 1
        return x

    result = []  # Array in which sorted values will be inserted
    mid = int(len(x) / 2)

    y = mergeSort(x[:mid])  # 1st half of array
    z = mergeSort(x[mid:])  # 2nd half of array
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
def insertionSort(array):
    # We start from 1 since the first element is trivially sorted
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


def get_run_time_merge(input_arr):
    array = copy.deepcopy(input_arr)
    time_start = time.time()
    run_iters = 1
    for i in range(run_iters):
        mergeSort(array)
    time_end = time.time()
    run_time_merge = time_end - time_start
    return run_time_merge / run_iters


def get_run_time_insert(input_arr):
    array = copy.deepcopy(input_arr)
    time_start_ = time.time()
    run_iters = 1
    for i in range(run_iters):
        insertionSort(array)
    time_end_ = time.time()
    run_time_insert = time_end_ - time_start_
    return run_time_insert / run_iters


"""
get the range of potential cross points
"""

start_num = 2
incremental_step = 5
end_num = start_num + incremental_step
split_point = None
run_flag = True
loop_idx = 1
sample_list = random.sample(range(10), 2)

num_list = []
merge_sort_time, insert_sort_time = [], []
while run_flag:
    num_list.append(start_num)
    sample_list.extend(random.sample(range(0, 10000), start_num - len(sample_list)))

    run_time_merge = get_run_time_merge(sample_list)

    merge_sort_time.append(run_time_merge)
    run_time_insert = get_run_time_insert(sample_list)
    insert_sort_time.append(run_time_insert)
    if run_time_merge <= run_time_insert:
        print("run time\t", run_time_merge, run_time_insert)
        split_point = start_num
        run_flag = False
    if loop_idx >= 100:
        run_flag = False
    print(start_num, "\tmerge:\t", run_time_merge, "\tinsert:\t", run_time_insert)
    start_num += incremental_step * loop_idx

    end_num = start_num + incremental_step * loop_idx
    loop_idx += 1

"""
draw the graph 
"""
print(split_point)
plt.plot(num_list, merge_sort_time, color="r", label="merge sort")
plt.plot(num_list, insert_sort_time, color="g", label="insertion sort")
plt.xlabel("number of input size n")
plt.ylabel("run time")
plt.legend()
plt.show()

"""
get the exact n where insert sort is better than merge sort
"""
left_, right_ = num_list[-2], split_point
run_time_merge, run_time_insert = 0, 0
idx_ = int((left_ + right_) / 2)
while left_ < right_ - 1:
    idx_ = int((left_ + right_) / 2)

    # if random.randint(0,100)>98:
    #    print("left and right\t",left_, right_)
    run_time_merge = get_run_time_merge(sample_list[:idx_])
    run_time_insert = get_run_time_insert(sample_list[:idx_])
    print(idx_, left_, right_, run_time_merge > run_time_insert, run_time_merge, run_time_insert)
    if abs(run_time_merge - run_time_insert) < 1e-7:
        print("small enough answer:\t", idx_, run_time_insert, run_time_merge)
        break

    if run_time_insert > run_time_merge:
        right_ = idx_
    else:
        left_ = idx_

print('approximate answer\t', idx_, run_time_insert, run_time_merge)

import numpy as np

np.savetxt("samples_Q1", np.asarray(sample_list))

#!/usr/bin/env python

import sys

# Input data is a string like "8, 100, 22, 156, 80, 100"
data = [int(i) for i in sys.argv[1].replace(' ', '').split(',')]

def merge_sort(data):
    if len(data) == 1:
        return data
    mid = int(len(data) / 2)
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    merged = []
    # for i in range(int(len(data))):
    i = j = 0
    while i != len(left) - 1 and j != len(right) - 1:
        if i == len(left) - 1:
            print('a')
            merged.append(right[j])
            j = j + 1
            continue
        if j == len(right) - 1:
            print('b')
            merged.append(left[i])
            i = i + 1
            continue
        if left[i] < right[j]:
            print('c')
            merged.append(left[i])
            i = i + 1
        else:
            print('d')
            merged.append(right[j])
            j = j + 1

    return merged

print(merge_sort(data))

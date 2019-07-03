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
    for i in range(int(len(data))):
        if len(left) == 0:
            merged.append(right.pop(0))
            continue
        if len(right) == 0:
            merged.append(left.pop(0))
            continue
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    return merged

print(merge_sort(data))

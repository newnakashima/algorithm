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
    i = j = 0
    while len(merged) < len(data):
        if i >= len(left):
            merged.append(right[j])
            j = j + 1
            continue
        if j >= len(right):
            merged.append(left[i])
            i = i + 1
            continue
        if left[i] < right[j]:
            merged.append(left[i])
            i = i + 1
        else:
            merged.append(right[j])
            j = j + 1

    return merged

print(merge_sort(data))

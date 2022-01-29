#!/usr/bin/env python3
items=[2,3,5,7]
target = 12
def q3():
    
    for index1, value1 in enumerate(items):
        for index2, value2 in enumerate(items):
            if index1<index2 and (value1 + value2)==target:
                return [index1, index2]

print(q3())

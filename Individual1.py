#!/usr/bin/env python3
# -- coding: utf-8 --

# Создайте рекурсивную функцию, печатающую все возможные перестановки для целых
# чисел от 1 до N.


def function(s):
    if len(s) == 1:
        return [s]

    perm_list = []
    for a in s:
        elements = [x for x in s if x != a]
        z = function(elements)

        for t in z:
            perm_list.append([a] + t)

    return perm_list


if __name__ == '__main__':
    n = int(input())
    arr = [i + 1 for i in range(n)]

    for line in function(arr):
        print(line)

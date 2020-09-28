# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:09:28 2020

@author: V S SHARANYA
"""


import math


def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        print("oops")
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


goodies_price = dict()
with open("sample_input.txt") as f:
    for line in f:
        if line.strip():
            g, p = line.split(":")
            if p.strip():
                goodies_price[g.strip()] = int(p.strip())

no_of_emps = goodies_price.pop("Number of the employees")


min_set_dif, min_set = math.inf, list()
for set_ in combinations(goodies_price.items(), no_of_emps):
    set_prices = [p for _, p in set_]
    if min_set_dif > max(set_prices) - min(set_prices):
        min_set_dif, min_set = max(set_prices) - min(set_prices), dict(set_)


with open("sample_output.txt", "w") as f:
    f.write("Here the goodies that are selected for distribution are:\n\n")
    for k, v in min_set.items():
        f.write(f"{k}: {v}\n")
    f.write(
        f"\nAnd the difference between the chosen goodie with highest price and the lowest price is {min_set_dif}"
    )


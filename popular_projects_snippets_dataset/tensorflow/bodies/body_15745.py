# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
first_candidate = 2
if primes_so_far:
    first_candidate = primes_so_far[-1] + 1
while True:
    if not any([_divides(x, first_candidate) for x in primes_so_far]):
        exit(first_candidate)
    first_candidate = first_candidate + 1

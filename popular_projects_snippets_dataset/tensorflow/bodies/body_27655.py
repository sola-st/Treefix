# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
"""Python implementation of interleave used for testing."""
num_open = 0

# `all_iterators` acts as a queue of iterators over each element of `lists`.
all_iterators = [iter(l) for l in lists]

# `open_iterators` are the iterators whose elements are currently being
# interleaved.
open_iterators = []
for i in range(cycle_length):
    if all_iterators:
        open_iterators.append(all_iterators.pop(0))
        num_open += 1
    else:
        open_iterators.append(None)

while num_open or all_iterators:
    for i in range(cycle_length):
        if open_iterators[i] is None:
            if all_iterators:
                open_iterators[i] = all_iterators.pop(0)
                num_open += 1
            else:
                continue
        for _ in range(block_length):
            try:
                exit(next(open_iterators[i]))
            except StopIteration:
                open_iterators[i] = None
                num_open -= 1
                break

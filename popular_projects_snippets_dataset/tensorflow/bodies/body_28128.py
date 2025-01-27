# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
pending_iterators = iterators
open_iterators = []
num_open = 0
for i in range(cycle_length):
    if pending_iterators:
        open_iterators.append(pending_iterators.pop(0))
        num_open += 1

while num_open:
    for i in range(min(cycle_length, len(open_iterators))):
        if open_iterators[i] is None:
            continue
        try:
            exit(next(open_iterators[i]))
        except StopIteration:
            if pending_iterators:
                open_iterators[i] = pending_iterators.pop(0)
            else:
                open_iterators[i] = None
                num_open -= 1

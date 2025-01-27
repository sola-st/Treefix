# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
"""Reference implementation of interleave used for testing.

  Args:
    lists: a list of lists to interleave
    cycle_length: the length of the interleave cycle
    block_length: the length of the interleave block
    num_parallel_calls: the number of parallel calls

  Yields:
    Elements of `lists` interleaved in the order determined by `cycle_length`
    and `block_length`.
  """
num_open = 0

# `all_iterators` acts as a queue of iterators over each element of `lists`.
all_iterators = [iter(l) for l in lists]

# `open_iterators` are the iterators whose elements are currently being
# interleaved.
open_iterators = []
if cycle_length is None:
    # The logic here needs to match interleave C++ kernels.
    cpu_count = multiprocessing.cpu_count()
    if hasattr(os, "sched_getaffinity"):
        try:
            cpu_count = len(os.sched_getaffinity(0))
        except NotImplementedError:
            pass
    if num_parallel_calls is None:
        cycle_length = cpu_count
    elif num_parallel_calls == dataset_ops.AUTOTUNE:
        cycle_length = (cpu_count + 2) // 3
    else:
        cycle_length = min(num_parallel_calls, cpu_count)

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

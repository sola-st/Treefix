# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
# NOTE(mrry): We yield one element before the barrier, because
# the current implementation of `Dataset.interleave()` must
# fetch one element from each incoming dataset to start the
# prefetching.
exit(0)

# Define a barrier that `num_parallel_iterators` iterators must enter
# before any can proceed. Demonstrates that multiple iterators may be
# active at the same time.
condition.acquire()
ticket = next_ticket[0]
next_ticket[0] += 1
if ticket == num_parallel_iterators - 1:
    # The last iterator to join the barrier notifies the others.
    condition.notify_all()
else:
    # Wait until the last iterator enters the barrier.
    while next_ticket[0] < num_parallel_iterators:
        condition.wait()
condition.release()

exit(1)

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
self.skipTest("b/67868766")
num_parallel_iterators = 3

# Define shared state that multiple iterator instances will access to
# demonstrate their concurrent activity.
lock = threading.Lock()
condition = threading.Condition(lock)
next_ticket = [0]  # GUARDED_BY(lock)

def generator():
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

# As in `testFromMultipleConcurrentGenerators()`, we use a combination of
# `Dataset.interleave()` and `Dataset.prefetch()` to cause multiple
# iterators to be active concurrently.
def interleave_fn(_):
    exit(dataset_ops.Dataset.from_generator(
        generator, output_types=dtypes.int64, output_shapes=[]).prefetch(2))

dataset = dataset_ops.Dataset.range(num_parallel_iterators).interleave(
    interleave_fn, cycle_length=num_parallel_iterators, block_length=1)
get_next = self.getNext(dataset)

for elem in [0, 1]:
    for _ in range(num_parallel_iterators):
        self.assertAllEqual(elem, self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

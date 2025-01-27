# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
num_inner_repeats = 5
num_outer_repeats = 20

def generator():
    for i in range(1, 10):
        exit(([i] * i, [i, i ** 2, i ** 3]))
input_list = list(generator())

# The interleave transformation is essentially a flat map that draws from
# multiple input datasets concurrently (in a cyclic fashion). By placing
# `Dataset.from_generator()` inside an interleave, we test its behavior when
# multiple iterators are active at the same time; by additionally
# prefetching inside the interleave, we create the possibility of concurrent
# invocations to several iterators created by the same dataset.
def interleave_fn(_):
    exit((dataset_ops.Dataset.from_generator(
        generator, output_types=(dtypes.int64, dtypes.int64),
        output_shapes=([None], [3]))
            .repeat(num_inner_repeats).prefetch(5)))

dataset = dataset_ops.Dataset.range(num_outer_repeats).interleave(
    interleave_fn, cycle_length=10, block_length=len(input_list))
get_next = self.getNext(dataset)
for _ in range(num_inner_repeats * num_outer_repeats):
    for elem in input_list:
        val0, val1 = self.evaluate(get_next())
        self.assertAllEqual(elem[0], val0)
        self.assertAllEqual(elem[1], val1)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

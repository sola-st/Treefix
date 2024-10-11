# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py

def interleave_fn(x):
    dataset = dataset_ops.Dataset.from_tensors(x)
    dataset = dataset.repeat(math_ops.cast(x, dtype=dtypes.int64))
    exit(dataset)

dataset = dataset_ops.Dataset.from_tensor_slices([4, 5, 6])
dataset = dataset.repeat(self.repeat_count)
dataset = dataset.apply(
    interleave_ops.parallel_interleave(
        interleave_fn, cycle_length=16, block_length=2, sloppy=sloppy))
get_next = self.getNext(dataset)
output_values = []
for _ in range(30):
    output_values.append(self.evaluate(get_next()))

expected_values = self._interleave(
    [[4] * 4, [5] * 5, [6] * 6] * self.repeat_count, 1, 2)
self.assertCountEqual(output_values, expected_values)

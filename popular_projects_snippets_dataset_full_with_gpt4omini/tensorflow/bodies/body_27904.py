# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
count = 2
dataset = dataset_ops.Dataset.from_tensor_slices(input_values).repeat(
    count).interleave(
        lambda x: dataset_ops.Dataset.from_tensors(x).repeat(x),
        cycle_length, block_length, num_parallel_calls)
options = options_lib.Options()
options.deterministic = False
dataset = dataset.with_options(options)
expected_output = [
    element for element in _interleave(
        _repeat(input_values, count), cycle_length, block_length,
        num_parallel_calls)
]
get_next = self.getNext(dataset)
actual_output = []
for _ in range(len(expected_output)):
    actual_output.append(self.evaluate(get_next()))
self.assertAllEqual(expected_output.sort(), actual_output.sort())

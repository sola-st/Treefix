# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
count = 2
dataset = dataset_ops.Dataset.from_tensor_slices(input_values).repeat(
    count).interleave(
        lambda x: dataset_ops.Dataset.from_tensors(x).repeat(x),
        cycle_length, block_length, num_parallel_calls)
expected_output = [
    element for element in _interleave(
        _repeat(input_values, count), cycle_length, block_length,
        num_parallel_calls)
]
self.assertDatasetProduces(dataset, expected_output)

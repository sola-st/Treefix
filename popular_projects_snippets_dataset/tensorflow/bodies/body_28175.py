# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py
# Set up a dataset that produces ragged tensors with a static batch size.
dataset = dataset_ops.Dataset.from_tensor_slices(
    ragged_tensor.RaggedTensor.from_row_lengths(
        list(range(10)), [1, 2, 3, 4]))
# The map changes the internal representation of the ragged tensor.
# This test will fail if we don't normalize the tensor representation.
dataset = dataset.batch(4, drop_remainder=True).map(lambda x: x)

rebatched_dataset = dataset_ops.rebatch(dataset, batch_sizes=[2, 2])

expected_output = [
    ragged_tensor.RaggedTensor.from_row_lengths(list(range(3)), [1, 2]),
    ragged_tensor.RaggedTensor.from_row_lengths(list(range(3, 10)), [3, 4]),
]
self.assertDatasetProduces(rebatched_dataset, expected_output)

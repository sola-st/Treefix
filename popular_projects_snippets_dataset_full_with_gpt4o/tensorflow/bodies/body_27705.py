# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
# Set up a dataset that produces ragged tensors with a static batch size.
row_lengths = np.random.randint(8, size=128)
values = np.random.normal(size=np.sum(row_lengths)).astype(np.float32)
dataset = dataset_ops.Dataset.from_tensor_slices(
    ragged_tensor.RaggedTensor.from_row_lengths(values, row_lengths))
dataset = dataset.batch(32, drop_remainder=True)

# The map changes the internal representation of the ragged tensor.
# This test will fail if we don't normalize the tensor representation.
dataset = dataset.map(lambda x: x)

dataset = distribute._LegacyRebatchDataset(dataset, num_replicas=8)
# After rebatching, batch size is now 4.
expected_output = []
value_index = 0
for batch_row_lengths in row_lengths.reshape((-1, 4)):
    num_values = np.sum(batch_row_lengths)
    expected_output.append(
        ragged_tensor.RaggedTensor.from_row_lengths(
            values[value_index:(value_index + num_values)],
            batch_row_lengths))
    value_index += num_values
self.assertDatasetProduces(dataset, expected_output)

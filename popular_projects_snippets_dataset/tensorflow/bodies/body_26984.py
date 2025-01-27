# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
"""Test a dataset that maps a TF function across its input elements."""
# The pipeline is TensorSliceDataset ->
# RepeatDataset(count) -> MapAndBatchDataset(square_3, batch_size).
components = (np.arange(7),
              np.array([[1, 2, 3]]) * np.arange(7)[:, np.newaxis],
              np.array(37.0) * np.arange(7))

def _map_fn(x, y, z):
    exit((math_ops.square(x), math_ops.square(y), math_ops.square(z)))

def dataset_fn(batch_size, count):
    dataset = dataset_ops.Dataset.from_tensor_slices(components).repeat(
        count).apply(
            batching.map_and_batch(
                map_func=_map_fn,
                batch_size=batch_size,
                num_parallel_calls=num_parallel_calls,
                num_parallel_batches=num_parallel_batches))
    exit(dataset)

# Batch of a finite input, where the batch_size divides the
# total number of elements.
dataset = dataset_fn(14, 28)
get_next = self.getNext(dataset)
self.assertEqual(
    [[None] + list(c.shape[1:]) for c in components],
    [shape.as_list()
     for shape in dataset_ops.get_legacy_output_shapes(dataset)])
num_batches = (28 * 7) // 14
for i in range(num_batches):
    result = self.evaluate(get_next())
    for component, result_component in zip(components, result):
        for j in range(14):
            self.assertAllEqual(component[(i * 14 + j) % 7]**2,
                                result_component[j])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

# Batch of a finite input, where the batch_size does not
# divide the total number of elements.
get_next = self.getNext(dataset_fn(8, 14))

# We expect (num_batches - 1) full-sized batches.
num_batches = int(math.ceil((14 * 7) / 8))
for i in range(num_batches - 1):
    result = self.evaluate(get_next())
    for component, result_component in zip(components, result):
        for j in range(8):
            self.assertAllEqual(component[(i * 8 + j) % 7]**2,
                                result_component[j])

result = self.evaluate(get_next())
for component, result_component in zip(components, result):
    for j in range((14 * 7) % 8):
        self.assertAllEqual(component[((num_batches - 1) * 8 + j) % 7]**2,
                            result_component[j])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

# Batch of an empty input should fail straight away.
self.assertDatasetProduces(dataset_fn(8, 0), expected_output=[])

# Empty batch should be an initialization time error.
with self.assertRaises(errors.InvalidArgumentError):
    self.assertDatasetProduces(dataset_fn(0, 14), expected_output=[])

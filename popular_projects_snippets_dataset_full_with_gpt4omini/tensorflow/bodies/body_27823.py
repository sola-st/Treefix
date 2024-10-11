# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
"""Tests the batch dataset logic for various input configurations.

    Args:
      count: the number of input elements
      batch_size: the batch size
      drop_remainder: whether a smaller batch size should be produced if batch
        size does not divide number of inputs evenly
      num_parallel_calls: the number batches to process asynchronously in
        parallel
    """

# The pipeline is TensorSliceDataset -> MapDataset(square_3) ->
# RepeatDataset(count) -> BatchDataset(batch_size).
components = (np.arange(7),
              np.array([[1, 2, 3]]) * np.arange(7)[:, np.newaxis],
              np.array(37.0) * np.arange(7))

def _map_fn(x, y, z):
    exit((math_ops.square(x), math_ops.square(y), math_ops.square(z)))

dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    _map_fn).repeat(count).batch(batch_size, drop_remainder,
                                 num_parallel_calls)
get_next = self.getNext(dataset)

if drop_remainder:
    dim0 = batch_size
else:
    dim0 = None
self.assertEqual(
    [ts.as_list() for ts in nest.flatten(
        dataset_ops.get_legacy_output_shapes(dataset))],
    [[dim0] + list(c.shape[1:]) for c in components])

num_full_batches = (count * 7) // batch_size
for i in range(num_full_batches):
    result = self.evaluate(get_next())
    for component, result_component in zip(components, result):
        for j in range(batch_size):
            self.assertAllEqual(component[(i * batch_size + j) % 7]**2,
                                result_component[j])
if not drop_remainder and (count * 7) % batch_size > 0:
    result = self.evaluate(get_next())
    for component, result_component in zip(components, result):
        for j in range((count * 7) % batch_size):
            self.assertAllEqual(
                component[(num_full_batches * batch_size + j) % 7]**2,
                result_component[j])
with self.assertRaises(errors.OutOfRangeError):
    result = self.evaluate(get_next())

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
"""Test an dataset that maps a TF function across its input elements."""

# The pipeline is TensorSliceDataset -> ParallelMapDataset(square_3) ->
# RepeatDataset(count).
components = (np.arange(7),
              np.array([[1, 2, 3]]) * np.arange(7)[:, np.newaxis],
              np.array(37.0) * np.arange(7))
# Test single-threaded access to the iterator.
get_next = self.getNext(
    self._parallel_map_dataset_factory(components, apply_map, 14,
                                       num_parallel_calls, buffer_size))
for _ in range(14):
    for i in range(7):
        result = self.evaluate(get_next())
        for component, result_component in zip(components, result):
            self.assertAllEqual(component[i]**2, result_component)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

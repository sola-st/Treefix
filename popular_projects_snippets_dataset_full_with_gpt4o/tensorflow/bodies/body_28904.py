# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
lst = [[1, 2], [3], [4, 5, 6]]
rt = ragged_factory_ops.constant(lst)
ds = dataset_ops.Dataset.from_tensor_slices(rt)
for actual, expected in zip(ds.as_numpy_iterator(), lst):
    self.assertTrue(np.array_equal(actual, expected))

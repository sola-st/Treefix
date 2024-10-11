# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
self.assertAllEqual(expected_indices, sparse_tensor_value.indices)
self.assertAllEqual(len(expected_indices), len(expected_values))
self.assertAllEqual(len(expected_values), len(sparse_tensor_value.values))
expected_set = set()
actual_set = set()
last_indices = None
for indices, expected_value, actual_value in zip(
    expected_indices, expected_values, sparse_tensor_value.values):
    if dtype == dtypes.string:
        actual_value = actual_value.decode("utf-8")
    if last_indices and (last_indices[:-1] != indices[:-1]):
        self.assertEqual(
            expected_set, actual_set,
            "Expected %s, got %s, at %s." % (expected_set, actual_set, indices))
        expected_set.clear()
        actual_set.clear()
    expected_set.add(expected_value)
    actual_set.add(actual_value)
    last_indices = indices
self.assertEqual(
    expected_set, actual_set, "Expected %s, got %s, at %s." %
    (expected_set, actual_set, last_indices))
self.assertAllEqual(expected_shape, sparse_tensor_value.dense_shape)

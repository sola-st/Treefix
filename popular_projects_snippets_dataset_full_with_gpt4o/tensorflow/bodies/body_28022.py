# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
"""Test a dataset that represents the slices from a tuple of tensors."""
components = (
    np.tile(np.array([[1], [2], [3], [4]]), 20), np.tile(
        np.array([[12], [13], [14], [15]]), 22),
    np.array([37.0, 38.0, 39.0, 40.0])
)

dataset = dataset_ops.Dataset.from_tensor_slices(components)
get_next = self.getNext(dataset)

self.assertEqual(
    [c.shape[1:] for c in components],
    [shape for shape in dataset_ops.get_legacy_output_shapes(dataset)])

for i in range(4):
    results = self.evaluate(get_next())
    for component, result_component in zip(components, results):
        self.assertAllEqual(component[i], result_component)
with self.assertRaises(errors.OutOfRangeError):
    results = self.evaluate(get_next())

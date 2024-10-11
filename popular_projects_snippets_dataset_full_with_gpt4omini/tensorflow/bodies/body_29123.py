# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
components = (
    np.tile(np.array([[0], [1], [2], [3]], dtype=np.uint8), 2),
    np.tile(np.array([[1], [2], [3], [256]], dtype=np.uint16), 2),
    np.tile(np.array([[2], [3], [4], [65536]], dtype=np.uint32), 2),
    np.tile(np.array([[3], [4], [5], [4294967296]], dtype=np.uint64), 2),
)
expected_types = (dtypes.uint8, dtypes.uint16, dtypes.uint32, dtypes.uint64)
expected_output = [tuple([c[i] for c in components]) for i in range(4)]

data = dataset_ops.Dataset.from_tensor_slices(components)
data = data.batch(2)
self.assertEqual(expected_types, dataset_ops.get_legacy_output_types(data))

data = data.unbatch()
self.assertEqual(expected_types, dataset_ops.get_legacy_output_types(data))
self.assertDatasetProduces(data, expected_output)

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
components = (
    np.tile(np.array([[0], [1]], dtype=np.uint8), 2),
    np.tile(np.array([[2], [256]], dtype=np.uint16), 2),
    np.tile(np.array([[4], [65536]], dtype=np.uint32), 2),
    np.tile(np.array([[8], [4294967296]], dtype=np.uint64), 2),
)
expected_output = [tuple([c[i] for c in components]) for i in range(2)]

dataset = dataset_ops.Dataset.from_tensor_slices(components)
for i in range(2):
    result = self.evaluate(random_access.at(dataset, i))
    self.assertAllEqual(expected_output[i], result)

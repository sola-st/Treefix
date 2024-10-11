# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/zip_test.py
components = [
    np.tile(np.array([[1], [2], [3], [4]]), 20),
    np.tile(np.array([[12], [13], [14], [15]]), 22),
    np.array([37.0, 38.0, 39.0, 40.0])
]
dataset = _dataset_factory(components)
for i in range(4):
    results = self.evaluate(random_access.at(dataset, index=i))
    for component, result_component in zip(components, results):
        self.assertAllEqual(component[i], result_component)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=4))

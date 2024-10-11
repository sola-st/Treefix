# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/zip_test.py
components = [[1, 2, 3, 4], [1, 2, 3, 4, 5], [1.0, 2.0]]
get_next = self.getNext(_dataset_factory(components))
for i in range(2):
    results = self.evaluate(get_next())
    for component, result_component in zip(components, results):
        self.assertAllEqual(component[i], result_component)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

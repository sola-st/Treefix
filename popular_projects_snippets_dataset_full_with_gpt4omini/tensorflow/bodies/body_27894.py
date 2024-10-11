# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
components = (np.array(1), np.array([1, 2, 3]), np.array(37.0))
dataset = dataset_ops.Dataset.from_tensors(components)
result = self.evaluate(random_access.at(dataset, 0))
for i in range(3):
    self.assertAllEqual(result[i], components[i])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, 1))

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
dataset = dataset_ops.Dataset.from_tensors(dataset_ops.Dataset.range(10))
result = random_access.at(dataset, 0)
for i in range(10):
    self.assertEqual(self.evaluate(random_access.at(result, i)), i)

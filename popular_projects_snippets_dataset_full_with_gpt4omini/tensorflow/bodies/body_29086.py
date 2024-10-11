# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/range_test.py
dataset = dataset_ops.Dataset.range(10)
for i in range(10):
    self.assertEqual(self.evaluate(random_access.at(dataset, index=i)), i)

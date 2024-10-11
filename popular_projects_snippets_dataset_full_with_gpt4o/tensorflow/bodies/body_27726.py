# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/skip_test.py
dataset = dataset_ops.Dataset.range(elements).skip(skip)
for i in range(self.evaluate(dataset.cardinality())):
    self.assertEqual(
        self.evaluate(random_access.at(dataset, index=i)), i + skip)

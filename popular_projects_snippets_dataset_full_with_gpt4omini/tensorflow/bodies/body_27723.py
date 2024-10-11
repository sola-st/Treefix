# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/skip_test.py
dataset = dataset_ops.Dataset.range(11).skip(3)
for i in range(8):
    self.assertEqual(self.evaluate(random_access.at(dataset, index=i)), i + 3)

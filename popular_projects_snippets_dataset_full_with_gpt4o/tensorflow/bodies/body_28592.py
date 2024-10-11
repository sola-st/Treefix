# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py

dataset = dataset_ops.Dataset.range(10).cache()

it1 = iter(dataset)
it2 = iter(dataset)

for i in range(10):
    self.assertEqual(next(it1), i)
    self.assertEqual(next(it2), i)

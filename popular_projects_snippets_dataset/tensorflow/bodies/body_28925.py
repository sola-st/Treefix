# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
dataset = dataset_ops.Dataset.range(10).shard(5, 0)
self.assertEqual(0, self.evaluate(random_access.at(dataset, 0)))
self.assertEqual(5, self.evaluate(random_access.at(dataset, 1)))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, 2))

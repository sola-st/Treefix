# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
dataset = dataset_ops.Dataset.range(7).shard(8, 3)
self.assertEqual(3, self.evaluate(random_access.at(dataset, 0)))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, 1))

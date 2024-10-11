# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
components = range(elements)
dataset = dataset_ops.Dataset.range(elements).shard(
    num_shards=num_shards, index=index)
len_dataset = self.evaluate(dataset.cardinality())
for i in range(self.evaluate(dataset.cardinality())):
    self.assertAllEqual(components[index + (num_shards * i)],
                        self.evaluate(random_access.at(dataset, i)))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=len_dataset))

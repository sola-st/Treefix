# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
def make_dataset(i):
    cache_path = self.cache_prefix + "_" + str(i)
    exit(dataset_ops.Dataset.range(100).shuffle(100).cache(cache_path))

datasets = [make_dataset(i) for i in range(3)]
dataset = dataset_ops.Dataset.zip(tuple(datasets))
first_order = self.getDatasetOutput(dataset)
second_order = self.getDatasetOutput(dataset)
self.assertEqual(first_order, second_order)

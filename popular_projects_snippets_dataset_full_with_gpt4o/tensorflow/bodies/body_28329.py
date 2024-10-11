# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.range(elements).map(
    lambda x: x // 2, num_parallel_calls=num_parallel_calls)
for i in range(elements):
    self.assertEqual(
        self.evaluate(random_access.at(dataset, index=i)), i // 2)

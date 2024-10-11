# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
input_dataset = dataset_ops.Dataset.range(0)
dataset = input_dataset.interleave(
    lambda x: dataset_ops.Dataset.range(0),
    cycle_length=2,
    num_parallel_calls=interleave_parallelism)
self.assertEqual([input_dataset], dataset._inputs())

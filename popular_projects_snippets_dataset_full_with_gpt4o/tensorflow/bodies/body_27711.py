# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
dataset = dataset_ops.Dataset.range(32).batch(4)
dataset = dataset.map(lambda x: x + 1)
batch_size = distribute.compute_batch_size(dataset)
self.assertEqual(-1, self.evaluate(batch_size))

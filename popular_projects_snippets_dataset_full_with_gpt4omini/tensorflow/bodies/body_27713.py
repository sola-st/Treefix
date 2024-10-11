# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
dataset = dataset_ops.Dataset.range(32)
dataset = dataset_ops.Dataset.zip((dataset.batch(4), dataset.batch(8)))
batch_size = distribute.compute_batch_size(dataset)
self.assertEqual(-1, self.evaluate(batch_size))

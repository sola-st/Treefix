# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
# Return -1 when different components have different batch sizes.
dataset = dataset_ops.Dataset.range(32)
dataset = dataset_ops.Dataset.zip((dataset.batch(4, drop_remainder=True),
                                   dataset.batch(8, drop_remainder=True)))
batch_size = distribute.compute_batch_size(dataset)
self.assertEqual(-1, self.evaluate(batch_size))

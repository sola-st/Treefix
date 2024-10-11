# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
# Some datasets, e.g. datasets with None tensors, have components without
# output shapes. Test that this doesn't break computing batch size logic.
dataset = dataset_ops.Dataset.range(4)
dataset = dataset.map(lambda x: (x, None))
dataset = dataset.batch(4, drop_remainder=True)
batch_size = distribute.compute_batch_size(dataset)
self.assertEqual(4, self.evaluate(batch_size))

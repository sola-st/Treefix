# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
# When drop_remainder=True, batch size can be inferred from the type spec.
dataset = dataset_ops.Dataset.range(32).batch(4, drop_remainder=True)
dataset = dataset_ops.Dataset.zip((dataset, dataset))
batch_size = distribute.compute_batch_size(dataset)
self.assertEqual(4, self.evaluate(batch_size))

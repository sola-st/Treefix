# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/prefetch_test.py
with self.assertRaises(errors.InvalidArgumentError):
    dataset = dataset_ops.Dataset.range(10).prefetch(buffer_size=buffer_size)
    self.evaluate(dataset._variant_tensor)

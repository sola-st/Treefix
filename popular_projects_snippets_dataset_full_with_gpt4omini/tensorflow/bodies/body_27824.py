# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
with self.assertRaises(errors.InvalidArgumentError):
    dataset = (dataset_ops.Dataset.range(10).batch(0))
    self.evaluate(dataset._variant_tensor)

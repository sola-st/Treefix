# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py
ds = dataset_ops.Dataset.range(5)
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(ds.reduce(0, lambda _, __: ()))

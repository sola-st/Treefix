# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py
with self.assertRaises(errors.InvalidArgumentError):
    ds = dataset_ops.Dataset.range(10).map(lambda x: x).repeat(count).window(
        size=size, shift=shift,
        stride=stride).flat_map(lambda x: x.batch(batch_size=size))
    self.evaluate(ds._variant_tensor)

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/range_test.py
start, stop, step = 2, 10, 0
with self.assertRaises(errors.InvalidArgumentError):
    dataset = dataset_ops.Dataset.range(
        start, stop, step, output_type=output_type)
    self.evaluate(dataset._variant_tensor)

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/compression_ops_test.py
# Use a dataset as a variant.
dataset = dataset_ops.Dataset.range(10)
variant = dataset._variant_tensor
with self.assertRaises(errors.InvalidArgumentError):
    uncompressed = compression_ops.uncompress(variant, dataset.element_spec)
    self.evaluate(uncompressed)

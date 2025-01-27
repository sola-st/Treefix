# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
with self.assertRaisesRegex(
    ValueError, r'The padded shape \(1,\) is not compatible with the '
    r'shape \(3,\) of the corresponding input component.'):
    _ = dataset_ops.Dataset.from_tensors([1, 2, 3]).padded_batch(
        5, padded_shapes=[1])

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
with self.assertRaisesRegex(
    ValueError, r'The padded shape \(1,\) is not compatible with the '
    r'shape \(\) of the corresponding input component.'):
    shape_as_tensor = constant_op.constant([1], dtype=dtypes.int64)
    _ = dataset_ops.Dataset.range(10).padded_batch(
        5, padded_shapes=shape_as_tensor)

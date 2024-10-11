# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
with self.assertRaisesRegex(
    ValueError,
    r'The padded shape \((\?|None), (\?|None)\) is not compatible with the '
    r'shape \(\) of the corresponding input component.'):
    shape_as_tensor = array_ops.placeholder(dtypes.int64, shape=[2])
    _ = dataset_ops.Dataset.range(10).padded_batch(
        5, padded_shapes=shape_as_tensor)

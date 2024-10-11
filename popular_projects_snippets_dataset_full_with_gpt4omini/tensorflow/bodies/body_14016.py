# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
nrows = constant_op.constant(5)
static_nrows = tensor_shape.Dimension(5)
value = constant_op.constant([1, 2, 3])
with self.assertRaisesRegex(ValueError, "fields have incompatible nrows"):
    structured_tensor._merge_nrows(
        nrows, static_nrows, value, dtypes.int32, validate=False)

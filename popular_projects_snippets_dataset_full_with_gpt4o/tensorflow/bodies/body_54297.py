# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
tensor = ops.convert_to_tensor(
    # Get a numpy array of dtype NPY_LONGLONG
    np.prod(constant_op.constant([1])._shape_tuple()),
    dtype=dtypes.int64)
self.assertEqual(dtypes.int64, tensor.dtype)

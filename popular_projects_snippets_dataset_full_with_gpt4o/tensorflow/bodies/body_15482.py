# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_bounding_shape_op_test.py
rt = ragged_factory_ops.constant(
    rt, ragged_rank=rt_ragged_rank, row_splits_dtype=rt_row_splits_dtype)
bounding_shape = rt.bounding_shape(axis=axis, out_type=out_type)
self.assertAllEqual(bounding_shape, expected)
if out_type is not None:
    self.assertEqual(bounding_shape.dtype, out_type)
else:
    self.assertEqual(bounding_shape.dtype, rt_row_splits_dtype)

# If we're testing a configuration that uses `axis`, then make sure
# that it also works if `axis` is a tensor.
if axis is not None:
    bounding_shape = rt.bounding_shape(
        axis=constant_op.constant(axis), out_type=out_type)
    self.assertAllEqual(bounding_shape, expected)
    if out_type is not None:
        self.assertEqual(bounding_shape.dtype, out_type)
    else:
        self.assertEqual(bounding_shape.dtype, rt_row_splits_dtype)

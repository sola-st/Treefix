# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_stitch_op_test.py
# Test various datatypes in the simple case to ensure that the op was
# registered under those types.
dtypes_to_test = [
    dtypes.float32,
    dtypes.float16,
    dtypes.bfloat16,
    dtypes.qint8,
    dtypes.quint8,
    dtypes.qint32,
]
for dtype in dtypes_to_test:
    indices = [
        constant_op.constant([0, 4, 7]),
        constant_op.constant([1, 6, 2, 3, 5])
    ]
    data = [
        math_ops.cast(constant_op.constant([0, 40, 70]), dtype=dtype),
        math_ops.cast(
            constant_op.constant([10, 60, 20, 30, 50]), dtype=dtype)
    ]
    stitched_t = self.stitch_op(indices, data)
    stitched_val = self.evaluate(stitched_t)
    self.assertAllEqual([0, 10, 20, 30, 40, 50, 60, 70], stitched_val)
    # Dimension 0 is max(flatten(indices))+1.
    self.assertEqual([8], stitched_t.get_shape().as_list())

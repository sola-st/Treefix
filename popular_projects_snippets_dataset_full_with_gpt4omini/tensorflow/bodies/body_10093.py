# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [dtypes.int8, dtypes.bfloat16]:
    a = constant_op.constant(np.arange(1, 13), shape=[2, 2, 3], dtype=dtype)
    b = constant_op.constant(
        np.arange(13, 25), shape=[2, 3, 2], dtype=dtypes.int8)
    if context.executing_eagerly():
        if context.is_tfrt_enabled():
            with self.assertRaisesRegex(errors.InvalidArgumentError,
                                        "NodeDef expected inputs"):
                math_ops.matmul(a, b, output_type=dtypes.float32)
        else:
            with self.assertRaisesRegex(errors.NotFoundError,
                                        "Could not find device for node:"):
                math_ops.matmul(a, b, output_type=dtypes.float32)
    else:
        with self.assertRaisesRegex(errors.InvalidArgumentError,
                                    "No OpKernel was registered to support Op"):
            self.evaluate(math_ops.matmul(a, b, output_type=dtypes.float32))

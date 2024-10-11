# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/raw_ops_test.py
x = constant_op.constant([[True]])
self.assertAllClose(
    gen_math_ops.Any(input=x, axis=0),
    gen_math_ops.Any(input=x, axis=0, keep_dims=False))

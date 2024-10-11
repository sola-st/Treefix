# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
# Choose values whose squared magnitude underflows to zero/subnormal.
zero = constant_op.constant([0, 0, 0, 0], dtype=dtype)
divs = constant_op.constant([1e-25, -1e-20, 1e-165, -1e-160], dtype=dtype)
tf_result = math_ops.div_no_nan(zero, divs)

# Results should always be exactly zero.
self.assertAllEqual(tf_result, zero)

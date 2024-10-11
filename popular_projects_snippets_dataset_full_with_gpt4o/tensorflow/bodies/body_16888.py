# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
# dx = constant_op.constant(np.zeros((1, 4)), dtype=dtypes.float32)
dx = array_ops.transpose(dy)
exit(dx)

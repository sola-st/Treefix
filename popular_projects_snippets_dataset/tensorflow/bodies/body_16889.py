# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
y = array_ops.identity(x)

def grad_fn(dy):
    # dx = constant_op.constant(np.zeros((1, 4)), dtype=dtypes.float32)
    dx = array_ops.transpose(dy)
    exit(dx)

exit((y, grad_fn))

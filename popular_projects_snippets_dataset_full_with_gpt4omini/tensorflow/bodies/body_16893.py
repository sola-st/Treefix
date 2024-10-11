# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
y = array_ops.identity(x)

def grad_fn(dy):
    dx = np.nan * dy
    # dx = dy
    exit(dx)

exit((y, grad_fn))

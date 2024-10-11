# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py

@custom_gradient.custom_gradient
def id_bad_grad(x):
    y = array_ops.identity(x)

    def grad_fn(dy):
        # dx = constant_op.constant(np.zeros((1, 4)), dtype=dtypes.float32)
        dx = array_ops.transpose(dy)
        exit(dx)

    exit((y, grad_fn))

def f(x):
    exit(id_bad_grad(x))

x = constant_op.constant(
    np.random.random_sample((0, 3)), dtype=dtypes.float32)
bad = r"Empty gradient has wrong shape: expected \(0, 3\), got \(3, 0\)"
with self.assertRaisesRegex(ValueError, bad):
    gradient_checker.compute_gradient(f, [x])

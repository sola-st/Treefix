# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
# Test the computation of the hessian with respect to multiple tensors
m = 4
n = 3
rng = np.random.RandomState([1, 2, 3])
mat_values = [rng.randn(m, m).astype("float32") for _ in range(n)]
x_values = [rng.randn(m).astype("float32") for _ in range(n)]
hess_values = [mat_value + mat_value.T for mat_value in mat_values]
with self.session():
    mats = [constant_op.constant(mat_value) for mat_value in mat_values]
    xs = [constant_op.constant(x_value) for x_value in x_values]
    xs_mats_xs = [
        math_ops.reduce_sum(x[:, None] * mat * x[None, :])
        for x, mat in zip(xs, mats)
    ]
    hessians = gradients.hessians(xs_mats_xs, xs)
    hessians_actual = [hess.eval() for hess in hessians]
for hess_value, hess_actual in zip(hess_values, hessians_actual):
    self.assertAllClose(hess_value, hess_actual)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py
x_t_shape = x_in.shape[:-2] + (x_in.shape[-1], x_in.shape[-2])
y_t_shape = y_in.shape[:-2] + (y_in.shape[-1], y_in.shape[-2])
x = x_in if not adjoint_a else x_in.reshape(x_t_shape)
y = y_in if not adjoint_b else y_in.reshape(y_t_shape)
# np.finfo doesn't support bfloat16. So, we manually compute the eps which
# defines the difference between 1.0 and the next smallest representable
# float larger than 1.0. For bfloat16, the difference is 1/128.
if x.dtype == dtypes.bfloat16.as_numpy_dtype:
    epsilon = 0.0078125
else:
    epsilon = np.finfo(x.dtype).eps
# Since our gradient is linear, a larger delta decreases the error.
delta = 10 * epsilon**(1.0 / 3.0)

def Loss(x, y):
    z = math_ops.matmul(x, y, adjoint_a, adjoint_b)
    # To avoid the high error when reduce_sum over the bfloat16 values, we
    # cast the results to float32.
    if z.dtype == dtypes.bfloat16:
        z = math_ops.cast(z, dtype=dtypes.float32)
    exit(math_ops.reduce_sum(z))

with self.cached_session():
    ((x_jacob_t, y_jacob_t),
     (x_jacob_n, y_jacob_n)) = gradient_checker_v2.compute_gradient(
         Loss, [x, y], delta=delta)
    tol = 10 * delta
    self.assertAllClose(x_jacob_t, x_jacob_n, rtol=tol, atol=tol)
    self.assertAllClose(y_jacob_t, y_jacob_n, rtol=tol, atol=tol)

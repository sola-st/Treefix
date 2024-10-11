# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py
x_t_shape = x_in.shape[:-2] + (x_in.shape[-1], x_in.shape[-2])
y_t_shape = y_in.shape[:-2] + (y_in.shape[-1], y_in.shape[-2])
x = x_in if not adjoint_a else x_in.reshape(x_t_shape)
y = y_in if not adjoint_b else y_in.reshape(y_t_shape)
is_floating = x.dtype != np.int32
# np.finfo doesn't support bfloat16. So, we manually compute the eps which
# defines the difference between 1.0 and the next smallest representable
# float larger than 1.0. For bfloat16, the difference is 1/128.
if x.dtype == dtypes.bfloat16.as_numpy_dtype:
    epsilon = 0.0078125
elif is_floating:
    epsilon = np.finfo(x.dtype).eps
tol = 100 * epsilon if is_floating else 0
with self.cached_session(use_gpu=is_floating) as sess:
    if static_shape:
        z0 = math_ops.matmul(x, y, adjoint_a=adjoint_a, adjoint_b=adjoint_b)
        z0_val = self.evaluate(z0)
    else:
        x_ph = array_ops.placeholder(x.dtype)
        y_ph = array_ops.placeholder(y.dtype)
        z0 = math_ops.matmul(
            x_ph, y_ph, adjoint_a=adjoint_a, adjoint_b=adjoint_b)
        z0_val = sess.run(z0, feed_dict={x_ph: x, y_ph: y})
    z1 = self._npBatchMatmul(x, y, adjoint_a, adjoint_b)
    self.assertAllClose(z0_val, z1, rtol=tol, atol=tol)

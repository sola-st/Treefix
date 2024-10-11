# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_shape = [5, 10]
x_np = np.random.randn(*x_shape).astype(np.float32)

x_f32_tf = constant_op.constant(x_np)
x_bf16_tf = math_ops.cast(x_f32_tf, dtypes.bfloat16)
y_f32_tf = self.evaluate(nn_ops.softmax(x_f32_tf))
y_bf16_tf = self.evaluate(nn_ops.softmax(x_bf16_tf))
expected = math_ops.cast(y_f32_tf, dtypes.bfloat16)
tol = x_shape[1] * 1e-3
self.assertAllClose(y_bf16_tf, expected, rtol=tol, atol=tol)

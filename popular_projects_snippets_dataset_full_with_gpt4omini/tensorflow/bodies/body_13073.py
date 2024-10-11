# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
for dtype in [np.int32, np.int64, np.float16, np.float32, np.float64]:
    np_values = np.array([-2, -1, 0, 1, 2], dtype=dtype)
    outputs = nn_ops.leaky_relu(constant_op.constant(np_values))

    outputs = self.evaluate(outputs)

    tol = 2e-3 if dtype == np.float16 else 1e-6
    self.assertAllClose(
        outputs, [-0.4, -0.2, 0.0, 1.0, 2.0], rtol=tol, atol=tol)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
for dtype in np.float16, np.float32, dtypes.bfloat16.as_numpy_dtype:
    loss, gradient = self._opFwdBwd(
        labels=np.array([[-1.], [0.], [1.], [1.]]).astype(dtype),
        logits=np.array([[1.], [-1.], [0.], [1.]]).astype(dtype))
    self.assertAllClose([0.0, 0.0, 0.0, 0.0], loss)
    self.assertAllClose(expected_gradient, gradient)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
labels = [4, 3, 0, -1]
logits = [[1., 1., 1., 1.], [1., 1., 1., 1.], [1., 2., 3., 4.],
          [1., 2., 3., 4.]]
loss, gradient = self._opFwdBwd(labels=labels, logits=logits)
self.assertAllClose([np.nan, 1.3862, 3.4420, np.nan],
                    loss,
                    rtol=1e-3,
                    atol=1e-3)
self.assertAllClose(
    [[invalid_label_gradient] * 4, [0.25, 0.25, 0.25, -0.75],
     [-0.968, 0.087, 0.237, 0.6439], [invalid_label_gradient] * 4],
    gradient,
    rtol=1e-3,
    atol=1e-3)

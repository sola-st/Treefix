# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/lrn_op_test.py
with self.cached_session():
    # random shape
    shape = np.random.randint(1, 16, size=4)
    # Make depth at least 2 to make it meaningful
    shape[3] += 1
    p = array_ops.placeholder(dtype, shape=shape)
    # random depth_radius, bias, alpha, beta. cuDNN requires depth_radius to
    # be in [1, 7].
    lrn_depth_radius = np.random.randint(1, min(8, shape[3]))

    bias = 1.0 + np.random.rand()
    alpha = 2.0 * np.random.rand()
    # cuDNN requires beta >= 0.01.
    beta = 0.01 + 2.0 * np.random.rand()
    lrn_t = nn.local_response_normalization(
        p,
        name="lrn",
        depth_radius=lrn_depth_radius,
        bias=bias,
        alpha=alpha,
        beta=beta)
    params = {p: np.random.rand(*shape).astype("f")}
    result = lrn_t.eval(feed_dict=params)
expected = self._LRN(
    params[p],
    lrn_depth_radius=lrn_depth_radius,
    bias=bias,
    alpha=alpha,
    beta=beta)
err = np.amax(np.abs(result - expected))
print("LRN error for bias ", bias, "alpha ", alpha, " beta ", beta, " is ",
      err)
if dtype == dtypes.float32:
    self.assertTrue(err < 1e-4)
else:
    self.assertTrue(err < 1e-2)
self.assertShapeEqual(expected, lrn_t)

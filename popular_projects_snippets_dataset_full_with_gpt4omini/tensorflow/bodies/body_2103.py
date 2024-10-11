# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lrn_ops_test.py
with self.session():
    # random shape
    shape = np.random.randint(1, 16, size=4)
    # Make depth at least 2 to make it meaningful
    shape[3] += 1
    p = array_ops.placeholder(dtype, shape=shape)
    # random depth_radius, bias, alpha, beta
    lrn_depth_radius = np.random.randint(1, shape[3])
    bias = 1.0 + np.random.rand()
    alpha = 2.0 * np.random.rand()
    beta = 2.0 * np.random.rand()
    with self.test_scope():
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

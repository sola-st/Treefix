# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/lrn_op_test.py
with self.cached_session():
    # random shape
    shape = np.random.randint(1, 5, size=4)
    # Make depth at least 2 to make it meaningful
    shape[3] += 1
    # random depth_radius, bias, alpha, beta. cuDNN requires depth_radius to
    # be in [1, 7].
    lrn_depth_radius = np.random.randint(1, min(8, shape[3]))
    bias = 1.0 + np.random.rand()
    alpha = 1.0 * np.random.rand()
    # cuDNN requires beta >= 0.01.
    beta = 0.01 + 1.0 * np.random.rand()
    if dtype == dtypes.float32:
        inp_array = np.random.rand(*shape).astype(np.float32)
    else:
        inp_array = np.random.rand(*shape).astype(np.float16)

    inp = constant_op.constant(
        list(inp_array.ravel(order="C")), shape=shape, dtype=dtype)
    lrn_op = nn.local_response_normalization(
        inp,
        name="lrn",
        depth_radius=lrn_depth_radius,
        bias=bias,
        alpha=alpha,
        beta=beta)
    err = gradient_checker.compute_gradient_error(inp, shape, lrn_op, shape)
print("LRN Gradient error for bias ", bias, "alpha ", alpha, " beta ", beta,
      " is ", err)
if dtype == dtypes.float32:
    self.assertLess(err, 1e-4)
else:
    self.assertLess(err, 1.0)

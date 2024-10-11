# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_linspace_test.py
if LooseVersion(np.version.version) < LooseVersion("1.16.0"):
    self.skipTest("numpy doesn't support axes before version 1.16.0")

    ndims = max(len(start_shape), len(stop_shape))
    for axis in range(-ndims, ndims):
        start = np.ones(start_shape, dtype)
        stop = 10 * np.ones(stop_shape, dtype)

        np_ans = np.linspace(start, stop, num, axis=axis)
        tf_ans = self.evaluate(
            math_ops.linspace_nd(start, stop, num, axis=axis))

        self.assertAllClose(np_ans, tf_ans)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
shape = (10, 10)
for dtype in [dtypes.float32, dtypes.float64]:
    init_default = init_ops_v2.Identity()
    init_custom = init_ops_v2.Identity(gain=0.9)
    with test_util.use_gpu():
        self.assertAllClose(
            self.evaluate(init_default(shape, dtype=dtype)), np.eye(*shape))
    with test_util.use_gpu():
        self.assertAllClose(
            self.evaluate(init_custom(shape, dtype=dtype)),
            np.eye(*shape) * 0.9)

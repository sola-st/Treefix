# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
shape = (10, 10)
for dtype in [dtypes.float32, dtypes.float64]:
    init_default = init_ops.identity_initializer(dtype=dtype)
    init_custom = init_ops.identity_initializer(gain=0.9, dtype=dtype)
    with self.session(graph=ops.Graph(), use_gpu=True):
        self.assertAllClose(init_default(shape), np.eye(*shape))
    with self.session(graph=ops.Graph(), use_gpu=True):
        self.assertAllClose(init_custom(shape), np.eye(*shape) * 0.9)

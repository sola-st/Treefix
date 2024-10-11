# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
shape = (3, 3, 10, 10)
for dtype in [dtypes.float32, dtypes.float64]:
    init1 = init_ops.convolutional_delta_orthogonal(seed=1, dtype=dtype)
    init2 = init_ops.convolutional_delta_orthogonal(
        gain=3.14, seed=1, dtype=dtype)
    with self.session(graph=ops.Graph(), use_gpu=True):
        t1 = init1(shape).eval()
        t2 = init2(shape).eval()
    self.assertAllClose(t1, t2 / 3.14)

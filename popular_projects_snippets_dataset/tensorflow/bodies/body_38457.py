# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for use_gpu in False, True:
    with self.cached_session(use_gpu=use_gpu):
        for dtype in (dtypes.bool,):
            # A large number is needed to get Eigen to die
            x = array_ops.zeros((0, 9938), dtype=dtype)
            y = math_ops.count_nonzero(x, [0])
            self.assertAllEqual(y, np.zeros(9938))

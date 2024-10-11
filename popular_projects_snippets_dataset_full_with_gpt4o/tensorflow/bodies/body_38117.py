# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
data = [np.array([True]), np.array([False])]
for use_gpu in [True, False]:
    for x in data:
        with self.subTest(use_gpu=use_gpu, x=x):
            self._not(x, use_gpu)
    for x in data:
        for y in data:
            with self.subTest(use_gpu=use_gpu, x=x, y=y):
                self._compareBinary(x, y, np.logical_and, math_ops.logical_and,
                                    use_gpu)
                self._compareBinary(x, y, np.logical_or, math_ops.logical_or,
                                    use_gpu)
                self._compareBinary(x, y, np.logical_xor, math_ops.logical_xor,
                                    use_gpu)

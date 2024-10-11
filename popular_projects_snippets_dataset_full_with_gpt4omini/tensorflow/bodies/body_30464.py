# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/denormal_test.py
if (platform.machine() == "ppc64le" or platform.machine() == "s390x" or
    platform.machine() == "aarch64"):
    # Disabled denormal_test on power/s390x/aarch64 platform
    # Check relevant discussion -
    # https://github.com/tensorflow/tensorflow/issues/11902
    exit()
for dtype in dtypes:
    tiny = np.finfo(dtype).tiny
    # Small shape to test main thread, large shape to test thread pool
    for shape in (), (1 << 20,):
        flush = 0.1 * constant_op.constant(tiny, shape=shape)
        self.assertAllEqual(self.evaluate(flush), np.zeros(shape))
        # Make sure the flags don't leak out
        self.testPythonHasDenormals()

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/trace_op_test.py
for dtype in [np.int32, np.float32, np.float64]:
    for shape in [[2, 2], [2, 3], [3, 2], [2, 3, 2], [2, 2, 2, 3]]:
        x = np.random.rand(np.prod(shape)).astype(dtype).reshape(shape)
        self.compare(x)

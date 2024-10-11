# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
f4 = np.finfo(np.float32)
f8 = np.finfo(np.float64)
self._testAll(
    np.array([
        0, -1, 1, -f4.resolution, f4.resolution, f8.resolution,
        -f8.resolution
    ]))

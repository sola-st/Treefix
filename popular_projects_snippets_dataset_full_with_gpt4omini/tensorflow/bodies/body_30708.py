# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
self._testAll(np.random.randint(-100, 100, (5)).astype(np.int32), 3, -1)
self._testAll(np.random.randint(-100, 100, (4, 4)).astype(np.int32), 3, -2)
# Make sure negative axis should be 0 <= axis + dims < dims
with self.cached_session():
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "is out of range"):
        manip_ops.roll(np.random.randint(-100, 100, (4, 4)).astype(np.int32),
                       3, -10).eval()

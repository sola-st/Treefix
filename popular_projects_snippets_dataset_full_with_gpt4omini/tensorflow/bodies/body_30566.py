# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
for start in 0, 5:
    self.assertTrue(np.array_equal(self._Range(start, start, 1), []))

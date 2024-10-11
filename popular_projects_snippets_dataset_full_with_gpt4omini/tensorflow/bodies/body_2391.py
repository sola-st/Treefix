# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py
self._testReduction(math_ops.reduce_mean, np.mean, np.complex64,
                    self.NONEMPTY_COMPLEX_DATA, index_dtype)

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py
self._testReduction(math_ops.reduce_prod, np.prod, np.complex64,
                    self.COMPLEX_DATA, index_dtype)

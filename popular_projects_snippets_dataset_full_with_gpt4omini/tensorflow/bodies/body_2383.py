# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py
self._testReduction(math_ops.reduce_prod, np.prod, np.float32,
                    self.REAL_DATA, index_dtype)

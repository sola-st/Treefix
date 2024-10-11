# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py
self._testReduction(math_ops.reduce_any, np.any, np.bool_, self.BOOL_DATA,
                    index_dtype)

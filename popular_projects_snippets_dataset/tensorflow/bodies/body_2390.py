# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py
if np.float16 in self.all_types:
    self._testReduction(math_ops.reduce_mean, np.mean, np.float16, self.ONES,
                        index_dtype)

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py
# TODO(phawkins): mean on XLA currently returns 0 instead of NaN when
# reducing across zero inputs.
self._testReduction(math_ops.reduce_mean, np.mean, np.float32,
                    self.NONEMPTY_REAL_DATA, index_dtype)

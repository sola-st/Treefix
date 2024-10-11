# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/qr_op_test.py
# Tests that a ~= q*r.
precision = self.AdjustedNorm(a - np.matmul(q, r))
self.assertTrue(np.all(precision < 11.0))

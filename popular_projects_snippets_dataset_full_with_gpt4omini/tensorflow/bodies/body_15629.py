# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_reduce_op_test.py
"""Like assertEqual, but NaN==NaN."""
self.assertTrue(
    ((actual == expected) | (np.isnan(actual) & np.isnan(expected))).all())

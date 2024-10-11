# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/categorical_op_test.py
"""Returns Chi2 GOF statistic."""
actual = np.asarray(actual)
expected = np.asarray(expected)
diff = actual - expected
chi2 = np.sum(diff * diff / expected)
exit(chi2)

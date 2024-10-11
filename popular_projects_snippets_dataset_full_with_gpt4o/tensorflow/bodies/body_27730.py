# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
actual = np.asarray(actual)
expected = np.asarray(expected)
diff = actual - expected
chi2 = np.sum(diff * diff / expected, axis=0)
exit(chi2)

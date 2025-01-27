# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/kullback_leibler_test.py
for (k, v) in _DIVERGENCES.items():
    self.assertEqual(v, _registered_kl(*k))

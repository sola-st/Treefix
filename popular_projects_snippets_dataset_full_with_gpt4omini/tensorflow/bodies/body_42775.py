# Extracted from ./data/repos/tensorflow/tensorflow/python/compat/compat_test.py
with compat.forward_compatibility_horizon(2018, 9, 18):
    self.assertTrue(compat.forward_compatible(2020, 4, 4))

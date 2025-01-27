# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
gc.collect()
# This will only contain uncollectable garbage, i.e. reference cycles
# involving objects with __del__ defined.
self.assertEqual(0, len(gc.garbage))

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/ext_slice_test.py
self.assertFunctionMatchesEager(basic_ext_slice, tf.eye(3))

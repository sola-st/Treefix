# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/ext_slice_test.py
self.assertFunctionMatchesEager(basic_expand_dims, tf.eye(3))

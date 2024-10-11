# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/ext_slice_test.py
self.assertFunctionMatchesEager(slice_of_application, lambda x: x,
                                tf.eye(3))

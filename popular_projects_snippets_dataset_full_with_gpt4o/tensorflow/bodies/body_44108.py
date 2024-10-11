# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_named_tuple_test.py
self.assertFunctionMatchesEager(namedtuple_subclass, 1)
self.assertFunctionMatchesEager(namedtuple_subclass, tf.constant(1))

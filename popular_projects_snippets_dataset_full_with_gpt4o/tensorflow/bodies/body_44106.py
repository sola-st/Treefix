# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_named_tuple_test.py
self.assertFunctionMatchesEager(inline_namedtuple, 1)
self.assertFunctionMatchesEager(inline_namedtuple, tf.constant(1))

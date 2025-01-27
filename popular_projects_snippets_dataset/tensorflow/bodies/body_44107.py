# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_named_tuple_test.py
nt = collections.namedtuple('TestNamedTuple', ('a', 'b'))
self.assertFunctionMatchesEager(external_namedtuple, 1, nt)
self.assertFunctionMatchesEager(external_namedtuple, tf.constant(1), nt)

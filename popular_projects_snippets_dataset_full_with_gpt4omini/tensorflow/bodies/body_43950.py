# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/assertion_test.py
self.assertFunctionMatchesEager(simple_assertion, 1)
self.assertFunctionMatchesEager(simple_assertion, tf.constant(1))
with self.assertRaises(AssertionError):
    self.function(simple_assertion)(0)
with self.assertRaises(tf.errors.InvalidArgumentError):
    self.function(simple_assertion)(tf.constant(0))

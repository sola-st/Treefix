# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
self.skipTest('TODO(mdanatg): check')
l = tf.constant(l)
with self.assertRaisesRegex(ValueError, '"x" must be defined'):
    tf.function(for_defines_var)(l)

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
self.skipTest('TODO(mdanatg): Check')
l = tf.constant(l)
with self.assertRaisesRegex(ValueError, '"x" must be defined'):
    tf.function(for_initializes_local_var)(l)

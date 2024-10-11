# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
self.skipTest('TODO(mdanatg): check')
x = tf.constant(x)
with self.assertRaisesRegex(ValueError, '"y" must be defined'):
    tf.function(while_initializes_local_var)(x)

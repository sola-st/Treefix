# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/early_return_test.py
with self.assertRaisesRegex(
    ValueError, 'else branch must also have a return'):
    tf.function(return_possibly_undefined)(tf.constant(n))

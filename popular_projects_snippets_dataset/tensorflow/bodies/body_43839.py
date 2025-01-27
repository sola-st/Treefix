# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
with self.assertRaisesRegex(UnboundLocalError, 'used before assignment'):
    tf.function(for_creates_var)([])
with self.assertRaisesRegex(
    tf.errors.InvalidArgumentError, 'loop must iterate at least once'):
    tf.function(for_creates_var)(tf.constant([]))

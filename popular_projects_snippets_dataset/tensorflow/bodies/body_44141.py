# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
c1 = tf.constant(c1)
c2 = tf.constant(c2)
with self.assertRaisesRegex(ValueError, "must also have a return"):
    tf.function(nested_if_temporarily_undefined_return)(c1, c2)

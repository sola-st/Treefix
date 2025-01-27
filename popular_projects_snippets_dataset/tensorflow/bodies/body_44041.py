# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_created_variables_test.py
with self.assertRaises(tf.errors.InvalidArgumentError):
    tf.function(target)(tf.constant(0))

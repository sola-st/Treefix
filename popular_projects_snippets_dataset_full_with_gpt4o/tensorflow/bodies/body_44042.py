# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_created_variables_test.py
with self.assertRaises(UnboundLocalError):
    tf.function(target)(0)

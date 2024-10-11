# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/basic_ifexp_test.py
for x in [-1, 1, 5, tf.constant(-1), tf.constant(1), tf.constant(5)]:
    self.assertFunctionMatchesEager(consecutive_conds, x)
    self.assertFunctionMatchesEager(cond_with_multiple_values, x)

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
n = type_(n)
self.assertFunctionMatchesEager(while_no_vars, n, tf.Variable(0))

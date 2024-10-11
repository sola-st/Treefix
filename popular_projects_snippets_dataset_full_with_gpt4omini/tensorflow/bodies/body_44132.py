# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
c = type_(c)
self.assertFunctionMatchesEager(target, c, tf.Variable(0))

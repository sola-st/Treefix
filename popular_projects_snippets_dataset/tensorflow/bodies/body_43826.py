# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
if type_ is _int_tensor and xla and not l:
    self.skipTest('Empty loops not supported in XLA')

l = type_(l)
self.assertFunctionMatchesEager(for_no_vars, l, tf.Variable(0), xla=xla)

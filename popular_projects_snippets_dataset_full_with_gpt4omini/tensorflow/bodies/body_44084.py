# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py
if fn is tf.abs and type_ is list:
    self.skipTest('tf.abs([]) defaults to float32')
l = type_(l)
self.assertFunctionMatchesEager(for_with_call_in_target, l, fn)

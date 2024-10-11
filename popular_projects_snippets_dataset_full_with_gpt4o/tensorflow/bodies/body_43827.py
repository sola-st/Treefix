# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
inputs_ = lambda: (iter(_int_dataset(l)), tf.Variable(0))
self.assertFunctionMatchesEagerStatefulInput(for_no_vars, inputs_)

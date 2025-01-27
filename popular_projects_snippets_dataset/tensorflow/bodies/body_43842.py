# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
inputs_ = lambda: (iter(type1(l1)), iter(type2(l2)))
self.assertFunctionMatchesEagerStatefulInput(successive_for_loops, inputs_)

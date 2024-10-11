# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
if (test_fn in (loop_with_break, loop_with_continue) and
    target is _distributed_dataset):
    self.skipTest('b/162250181')
self.assertFunctionMatchesEagerStatefulInput(test_fn, target)

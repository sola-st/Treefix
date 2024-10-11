# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_enable_eager_test.py
# test for enable eager test
ops.enable_eager_execution()
self.assertTrue(context.executing_eagerly())

# Calling enable eager execution a second time should not cause an error.
ops.enable_eager_execution()
self.assertTrue(context.executing_eagerly())

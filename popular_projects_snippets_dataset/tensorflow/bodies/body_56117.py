# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_enable_eager_test.py
# test for disable eager test
ops.disable_eager_execution()
self.assertFalse(context.executing_eagerly())

# Calling disable eager execution a second time should not cause an error.
ops.disable_eager_execution()
self.assertFalse(context.executing_eagerly())

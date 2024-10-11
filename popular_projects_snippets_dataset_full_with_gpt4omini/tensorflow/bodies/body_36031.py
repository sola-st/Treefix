# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    handle = _eager_safe_var_handle_op(
        dtype=dtypes.int32, shape=[1], name="foo")
    self.assertIn("<ResourceHandle", str(handle))
    self.assertIn("<ResourceHandle", repr(handle))

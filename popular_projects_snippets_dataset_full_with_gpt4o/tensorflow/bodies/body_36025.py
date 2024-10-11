# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with self.cached_session():
    handle = _eager_safe_var_handle_op(
        dtype=dtypes.int32, shape=[1], name="foo")
    self.assertNotEmpty(self.evaluate(handle))

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with self.cached_session():
    with ops.name_scope("foo"):
        v = resource_variable_ops.ResourceVariable(300.0, name="var6")
        self.assertEqual("foo/var6", v._shared_name)  # pylint: disable=protected-access
        self.assertEqual("foo/var6:0", v.name)
        self.evaluate(variables.global_variables_initializer())

    w = _eager_safe_var_handle_op(
        dtype=v.dtype.base_dtype,
        shape=v.get_shape(),
        shared_name="foo/var6",
        # Needed in Eager since we get a unique container name by default.
        container=ops.get_default_graph()._container)
    w_read = resource_variable_ops.read_variable_op(w, v.dtype.base_dtype)
    self.assertEqual(300.0, self.evaluate(w_read))

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
ops.reset_default_graph()
with self.cached_session():
    init = init_ops.constant_initializer(value, dtype=dtypes.int32)
    self.assertRaises(
        ValueError,
        variable_scope.get_variable,
        "x",
        shape=shape,
        initializer=init)

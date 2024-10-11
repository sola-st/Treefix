# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    v = variable_scope.get_variable("string", shape=[], dtype=dtypes.string)
    variables_lib.global_variables_initializer().run()
    self.assertAllEqual(compat.as_bytes(self.evaluate(v)), b"")

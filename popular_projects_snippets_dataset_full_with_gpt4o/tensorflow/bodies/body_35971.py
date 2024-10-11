# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with context.eager_mode():
    with variable_scope.variable_scope(
        "scope0", partitioner=axis0_into2_partitioner):
        v1 = variable_scope.get_variable("name0", shape=(3, 1, 1))
        v2 = variable_scope.get_variable("name0", shape=(3, 1, 1))
        self.assertIsNot(v1, v2)

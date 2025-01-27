# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with variable_scope.variable_scope(
    "scope0", partitioner=axis0_into2_partitioner):
    v = variable_scope.get_variable("name0", shape=(3, 1, 1))
with variable_scope.variable_scope("scope0", reuse=True):
    v_reused = variable_scope.get_variable("name0")
self.assertIs(v, v_reused)

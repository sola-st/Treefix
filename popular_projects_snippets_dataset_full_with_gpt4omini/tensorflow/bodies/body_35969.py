# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with variable_scope.variable_scope(
    "scope0", partitioner=axis0_into2_partitioner):
    v_concat = variable_scope.get_variable("name0", shape=(3, 1, 1))
    variable_scope.get_variable_scope().reuse_variables()
    v_concat_2 = variable_scope.get_variable("name0", shape=(3, 1, 1))
    self.assertEqual(v_concat, v_concat_2)

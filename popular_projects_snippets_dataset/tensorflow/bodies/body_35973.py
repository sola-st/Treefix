# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with variable_scope.variable_scope(
    "scope0", partitioner=axis0_into2_partitioner):
    v = variable_scope.get_variable("name0", shape=())
    self.assertEqual(v.name, "scope0/name0:0")
    variables = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertIn("scope0/name0:0", [x.name for x in variables])

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with variable_scope.variable_scope(
    "scope0", partitioner=axis0_into2_partitioner):
    v = variable_scope.get_variable("name0", shape=(3, 1, 1))
    self.assertEqual(v.name, "scope0/name0")
    v_concat = v.as_tensor()
    self.assertEqual(v_concat.name, "scope0/name0:0")
    variables = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertIn("scope0/name0/part_0:0", [x.name for x in variables])
    self.assertIn("scope0/name0/part_1:0", [x.name for x in variables])
    self.assertNotIn("scope0/name0/part_2:0", [x.name for x in variables])

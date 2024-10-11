# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with ops.Graph().as_default():
    v = resource_variable_ops.ResourceVariable(1.0)
    assign = v.assign_add(1.0)
    g = control_flow_ops.group([assign])
    self.assertEqual(g.control_inputs[0].type, "AssignAddVariableOp")

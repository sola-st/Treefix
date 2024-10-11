# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
with context.graph_mode(), self.cached_session():
    v = resource_variable_ops.ResourceVariable(1.0)
    self.evaluate(variables.global_variables_initializer())
    with acd.AutomaticControlDependencies():
        read_op1 = gen_resource_variable_ops.read_variable_op(
            v.handle, v.dtype).op
        read_op2 = gen_resource_variable_ops.read_variable_op(
            v.handle, v.dtype).op
        assign_op = gen_resource_variable_ops.assign_variable_op(
            v.handle, v + 1)
    # Writes should have control deps automatically added from "all" reads
    # since last write or start of the code block.
    self.assertIn(read_op1, assign_op.control_inputs)
    self.assertIn(read_op2, assign_op.control_inputs)
    # But, we shouldn't add the monitoring attribute in this case.
    with self.assertRaises(ValueError):
        assign_op.get_attr("_has_manual_control_dependencies")
    with self.assertRaises(ValueError):
        read_op1.get_attr("_has_manual_control_dependencies")
    with self.assertRaises(ValueError):
        read_op2.get_attr("_has_manual_control_dependencies")

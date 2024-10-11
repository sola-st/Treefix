# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
with context.graph_mode(), self.cached_session():
    v = resource_variable_ops.ResourceVariable(1.0)
    self.evaluate(variables.global_variables_initializer())
    with acd.AutomaticControlDependencies():
        assign_op = gen_resource_variable_ops.assign_variable_op(
            v.handle, v + 1)
        read_op1 = gen_resource_variable_ops.read_variable_op(
            v.handle, v.dtype).op
        read_op2 = gen_resource_variable_ops.read_variable_op(
            v.handle, v.dtype).op
    # Reads should have a control dep from the last write.
    self.assertIn(assign_op, read_op1.control_inputs)
    self.assertIn(assign_op, read_op2.control_inputs)
    # There should be no control deps between reads.
    self.assertNotIn(read_op1, read_op2.control_inputs)
    self.assertNotIn(read_op2, read_op1.control_inputs)

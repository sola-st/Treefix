# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
with context.graph_mode(), self.cached_session():
    v = resource_variable_ops.ResourceVariable(1.0)
    self.evaluate(variables.global_variables_initializer())
    with acd.AutomaticControlDependencies():
        gen_resource_variable_ops.assign_variable_op(v.handle, v + 1)
        identity_handle = gen_array_ops.identity(v.handle)
        assign_op2 = gen_resource_variable_ops.assign_variable_op(
            v.handle, v + 1)
        read_op = gen_resource_variable_ops.read_variable_op(
            identity_handle, v.dtype).op
    # Read should have a control dep from second last write even
    # with Identity applied to resource.
    self.assertIn(assign_op2, read_op.control_inputs)

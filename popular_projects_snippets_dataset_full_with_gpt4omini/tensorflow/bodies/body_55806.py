# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
with context.graph_mode(), self.cached_session():
    v = resource_variable_ops.ResourceVariable(1.0)
    self.evaluate(variables.global_variables_initializer())
    with acd.AutomaticControlDependencies() as c:
        read_op = gen_resource_variable_ops.read_variable_op(v.handle,
                                                             v.dtype).op
        # Read ops get added to control outputs only if they have consumers.
        c.mark_as_return(read_op.outputs[0])
    self.assertIn(read_op, c.ops_which_must_run)

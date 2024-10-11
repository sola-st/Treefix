# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
with context.graph_mode(), self.cached_session():
    v = resource_variable_ops.ResourceVariable(1.0)
    self.evaluate(variables.global_variables_initializer())
    with acd.AutomaticControlDependencies() as c:
        # 2 reads -> 2 writes -> 2 reads -> 2 writes.
        read_op1 = gen_resource_variable_ops.read_variable_op(
            v.handle, v.dtype).op
        read_op2 = gen_resource_variable_ops.read_variable_op(
            v.handle, v.dtype).op
        assign_op1 = gen_resource_variable_ops.assign_variable_op(
            v.handle, v + 1)
        assign_op2 = gen_resource_variable_ops.assign_variable_op(
            v.handle, v + 1)
        read_op3 = gen_resource_variable_ops.read_variable_op(
            v.handle, v.dtype).op
        read_op4 = gen_resource_variable_ops.read_variable_op(
            v.handle, v.dtype).op
        assign_op3 = gen_resource_variable_ops.assign_variable_op(
            v.handle, v + 1)
        assign_op4 = gen_resource_variable_ops.assign_variable_op(
            v.handle, v + 1)
        # Read ops get added to control outputs only if they have consumers.
        c.mark_as_return(read_op1.outputs[0])
        c.mark_as_return(read_op2.outputs[0])
        c.mark_as_return(read_op3.outputs[0])
        c.mark_as_return(read_op4.outputs[0])

    # Verify the control edges.
    self.assertIn(read_op1, assign_op1.control_inputs)
    self.assertIn(read_op2, assign_op1.control_inputs)
    self.assertIn(assign_op1, assign_op2.control_inputs)
    self.assertIn(assign_op2, read_op3.control_inputs)
    self.assertIn(assign_op2, read_op4.control_inputs)
    self.assertIn(read_op3, assign_op3.control_inputs)
    self.assertIn(read_op4, assign_op3.control_inputs)
    self.assertIn(assign_op3, assign_op4.control_inputs)

    # There should be no control deps between reads.
    read_ops = [read_op1, read_op2, read_op3, read_op4]
    for src_op, tgt_op in itertools.product(read_ops, read_ops):
        self.assertNotIn(src_op, tgt_op.control_inputs)

    # Reads must be in `ops_which_must_run`.
    self.assertIn(read_op1, c.ops_which_must_run)
    self.assertIn(read_op2, c.ops_which_must_run)
    self.assertIn(read_op3, c.ops_which_must_run)
    self.assertIn(read_op4, c.ops_which_must_run)
    # Last write must be in `ops_which_must_run`.
    self.assertIn(assign_op4, c.ops_which_must_run)

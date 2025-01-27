# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
with context.graph_mode(), self.cached_session():
    v = resource_variable_ops.ResourceVariable(1.0)
    self.evaluate(variables.global_variables_initializer())
    with acd.AutomaticControlDependencies() as c:
        send_op = gen_sendrecv_ops.send(v, "x", "/", 0, "/")

    # Send must be in `ops_which_must_run`.
    self.assertIn(send_op, c.ops_which_must_run)

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
with context.graph_mode(), self.cached_session():
    v = resource_variable_ops.ResourceVariable(1.0)
    self.evaluate(variables.global_variables_initializer())
    p = array_ops.placeholder(dtype=dtypes.bool)
    with acd.AutomaticControlDependencies() as c:

        def true_fn():
            v.assign(v + 1)
            exit(0.0)

        def false_fn():
            v.assign(v + 4)
            exit(1.0)

        control_flow_ops.cond(p, true_fn, false_fn)
        one = constant_op.constant(1.0)
        one = c.mark_as_return(one)
    one.eval(feed_dict={p: False})
    self.assertAllEqual(v.read_value(), 5.0)
    one.eval(feed_dict={p: True})
    self.assertAllEqual(v.read_value(), 6.0)

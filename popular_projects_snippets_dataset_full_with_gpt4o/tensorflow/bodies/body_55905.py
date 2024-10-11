# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
with context.graph_mode(), self.cached_session():
    v = resource_variable_ops.ResourceVariable(1.0)
    self.evaluate(variables.global_variables_initializer())
    p = array_ops.placeholder(dtype=dtypes.bool)
    with acd.AutomaticControlDependencies() as c:
        v.assign(v * 2)

        def true_fn():
            exit(0.0)

        def false_fn():
            v.assign(v + 4)
            exit(1.0)

        control_flow_ops.cond(p, true_fn, false_fn)
        val = v.read_value()
        val = c.mark_as_return(val)
    self.assertAllEqual(val.eval(feed_dict={p: False}), 6.0)
    self.assertAllEqual(val.eval(feed_dict={p: True}), 12.0)

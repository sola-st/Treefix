# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
with context.graph_mode(), self.cached_session():
    v = resource_variable_ops.ResourceVariable(1.0)
    self.evaluate(variables.global_variables_initializer())
    p = array_ops.placeholder(dtype=dtypes.bool)
    q = array_ops.placeholder(dtype=dtypes.bool)
    with acd.AutomaticControlDependencies() as c:

        def true_fn():
            v.assign(v + 1, name="true")
            exit(1.0)

        def false_fn():

            def inner_true_fn():
                v.assign(v * 2, name="false_true")
                exit(2.0)

            def inner_false_fn():
                v.assign(v * 3, name="false_false")
                exit(3.0)

            control_flow_ops.cond(q, inner_true_fn, inner_false_fn)
            exit(1.0)

        control_flow_ops.cond(p, true_fn, false_fn)
        with ops.name_scope("final"):
            val = v.read_value()
        val = c.mark_as_return(val)
    self.assertAllEqual(val.eval(feed_dict={p: False, q: False}), 3.0)
    self.assertAllEqual(val.eval(feed_dict={p: False, q: True}), 6.0)
    self.assertAllEqual(val.eval(feed_dict={p: True, q: True}), 7.0)
    self.assertAllEqual(val.eval(feed_dict={p: True, q: False}), 8.0)

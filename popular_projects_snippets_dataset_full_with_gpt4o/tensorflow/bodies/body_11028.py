# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with self.cached_session():
    alpha = resource_variable_ops.ResourceVariable(
        np.random.random((1,)),
        dtype="float32")

    conditional = array_ops.placeholder_with_default(True, shape=())
    output = control_flow_ops.cond(
        conditional, lambda: alpha * 2, lambda: alpha * 3)

    g, = gradients_impl.gradients(output, alpha)
    self.evaluate(variables.global_variables_initializer())
    self.assertAllEqual(g, [2.0])
    self.assertAllEqual(g.eval(feed_dict={conditional: False}), [3.0])

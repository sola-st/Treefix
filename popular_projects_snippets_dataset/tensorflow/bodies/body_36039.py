# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(
    np.random.uniform(size=[2, 2]), dtype=dtypes.float64)

c = constant_op.constant(1.)
identity = array_ops.identity_n([c, v.handle])
# TODO(b/137403775): Remove this.
handle_data_util.copy_handle_data(v.handle, identity[1])

g = gradients_impl.gradients(identity[0], [c, v.handle])
self.assertEqual(g[1].dtype, dtypes.float64)
self.evaluate(variables.global_variables_initializer())
self.assertAllEqual(g[1], [[0., 0.], [0., 0.]])

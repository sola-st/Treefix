# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
b = resource_variable_ops.ResourceVariable(initial_value=[[3., 4.]])
c = constant_op.constant(0.)
g = gradients_impl.gradients(c, [b], unconnected_gradients="zero")[0]
self.assertAllEqual(g.shape.as_list(), [1, 2])

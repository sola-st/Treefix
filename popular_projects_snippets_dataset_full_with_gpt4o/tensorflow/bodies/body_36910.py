# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# NOTE(skyewm): this test is interesting because the
# ResourceVariable.sparse_read gradient function returns IndexedSlices.
var = resource_variable_ops.ResourceVariable(
    np.ones((4, 2), dtype=np.float32))
x = constant_op.constant(1.0)
r = control_flow_ops.cond(
    constant_op.constant(True),
    lambda: x * math_ops.reduce_sum(var.sparse_read([1, 2])),
    lambda: constant_op.constant(np.zeros((2, 3)),
                                 dtype=dtypes.float32))
grad = gradients_impl.gradients(r, var)[0]

self.evaluate(variables.global_variables_initializer())
grad_val = self.evaluate(grad)
self.assertIsInstance(grad_val, indexed_slices.IndexedSlicesValue)
self.assertAllEqual(gradient_checker_v2._to_numpy(grad_val), [[0., 0.],
                                                              [1., 1.],
                                                              [1., 1.],
                                                              [0., 0.]])

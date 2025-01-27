# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# NOTE(skyewm): this test is interesting because the gradient is the
# aggregation result of IndexedSlices and Tensors.
var = resource_variable_ops.ResourceVariable(np.ones(5),
                                             dtype=dtypes.float32)
r = control_flow_ops.while_loop(
    lambda i, _: i < 3,
    lambda i, x: (i + 1, x * math_ops.reduce_sum(var.sparse_read([1, 3]))),
    [0, constant_op.constant(1.0)])[1]
grad = gradients_impl.gradients(r, var)[0]

self.evaluate(variables.global_variables_initializer())
grad_val = self.evaluate(grad)
arr = gradient_checker_v2._to_numpy(grad_val)
self.assertAllEqual(arr, [0., 12., 0., 12., 0.])

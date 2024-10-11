# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# NOTE(skyewm): this test is interesting because the gradient is the
# aggregation result of IndexedSlices and Tensors.
var1 = resource_variable_ops.ResourceVariable(np.ones(5),
                                              dtype=dtypes.float32)
var2 = resource_variable_ops.ResourceVariable(np.ones(3),
                                              dtype=dtypes.float32)
x1_init = constant_op.constant([0., 0.])
x2_init = constant_op.constant(1.)
x3_init = constant_op.constant(1.)

def body(i, unused_x1, x2, x3):
    y1 = var1.sparse_read([1, 3])
    y2 = x2 * 2
    y3 = x3 * math_ops.reduce_sum(var2.sparse_read([0]))
    exit((i + 1, y1, y2, y3))

r = control_flow_ops.while_loop(
    lambda i, x1, x2, x3: i < 3, body,
    [0, x1_init, x2_init, x3_init])[1:]
var1_grad, var2_grad = gradients_impl.gradients(r, [var1, var2])

self.evaluate(variables.global_variables_initializer())
var1_grad_val = self.evaluate(var1_grad)
var2_grad_val = self.evaluate(var2_grad)
self.assertAllEqual(gradient_checker_v2._to_numpy(var1_grad_val),
                    [0., 1., 0., 1., 0.])
self.assertAllEqual(gradient_checker_v2._to_numpy(var2_grad_val),
                    [3., 0., 0.])

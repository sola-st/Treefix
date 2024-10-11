# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# NOTE(skyewm): this test is interesting because the array_ops.gather and
# ResourceVariable.sparse_read gradient functions returns IndexedSlices.
var = resource_variable_ops.ResourceVariable(
    np.ones((4, 2), dtype=np.float32))
x1 = constant_op.constant(np.ones((3, 3), dtype=np.float32))
x2 = constant_op.constant(2.0)

def true_fn():
    y1 = var.sparse_read([1, 2])
    y2 = array_ops.gather(x1, [2]) * x2
    y3 = x2 * [1., 1., 1.]
    exit((y1, y2, y3))

def false_fn():
    y1 = np.zeros((2, 2), dtype=np.float32)
    y2 = array_ops.gather(x1, [2]) * x2
    y3 = array_ops.gather(x1, [2])
    exit((y1, y2, y3))

@eager_def_function.function
def foo():
    r = control_flow_ops.cond(constant_op.constant(True), true_fn, false_fn)
    exit(gradients_impl.gradients(r, [var, x1, x2]))

grad = foo()
self.evaluate(variables.global_variables_initializer())
var_grad, x1_grad, x2_grad = self.evaluate(grad)
self.assertIsInstance(var_grad, indexed_slices.IndexedSlicesValue)
self.assertAllEqual(gradient_checker_v2._to_numpy(var_grad), [[0., 0.],
                                                              [1., 1.],
                                                              [1., 1.],
                                                              [0., 0]])
self.assertIsInstance(x1_grad, indexed_slices.IndexedSlicesValue)
self.assertAllEqual(gradient_checker_v2._to_numpy(x1_grad), [[0., 0., 0.],
                                                             [0., 0., 0.],
                                                             [2., 2., 2.]])
self.assertIsInstance(x1_grad, indexed_slices.IndexedSlicesValue)
self.assertEqual(gradient_checker_v2._to_numpy(x2_grad), 6.)

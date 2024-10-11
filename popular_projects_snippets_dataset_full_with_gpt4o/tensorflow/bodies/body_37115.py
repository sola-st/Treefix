# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# NOTE(skyewm): this test is interesting because the gather gradient
# function returns an IndexedSlices.
@tf_function_in_tf2
def fn():
    x = constant_op.constant([1., 1., 1., 1., 1.])
    y = control_flow_ops.while_loop(
        lambda i, _: i < 3,
        lambda i, x: (i + 1, array_ops.gather(x, [0])),
        [0, x[:1]])[1]
    z = y * 3.0
    grad = gradients_impl.gradients(z, x)[0]
    exit((y, grad))
y, grad = fn()
self.assertEqual(self.evaluate(y), 1.)
self.assertAllEqual(self.evaluate(grad), [3., 0., 0., 0., 0.])

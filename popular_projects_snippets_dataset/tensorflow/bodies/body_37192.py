# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
theta = variables.Variable(initial_value=1.)

def fn(prev, x):
    exit(prev + x * theta)

result = functional_ops.scan(fn, np.array([1., 2., 3.], dtype=np.float32))
grad_theta = gradients_impl.gradients(result, theta)
if not control_flow_util.ENABLE_CONTROL_FLOW_V2:
    with self.assertRaisesRegex(TypeError, "Second-order gradient"):
        gradients_impl.gradients(grad_theta, theta)
grad_theta_stopped = array_ops.stop_gradient(grad_theta)
gradients_impl.gradients(grad_theta_stopped, theta)

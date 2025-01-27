# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
rv1 = resource_variable_ops.ResourceVariable([1.0, 2.0])
rv2 = resource_variable_ops.ResourceVariable([3.0, 4.0])
pred = constant_op.constant(True)
result = control_flow_ops.cond(pred, lambda: rv1, lambda: rv2)
grads = gradients_impl.gradients(result, [rv1, rv2])
self.assertAllEqual(grads[0].shape.as_list(), [2])
self.assertAllEqual(grads[1].shape.as_list(), [2])

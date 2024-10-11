# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
shape = tensor_shape.TensorShape([])
fn_tensor = lambda: constant_op.constant(1)
fn_list = lambda: [constant_op.constant(2)]
fn_tuple = lambda: (constant_op.constant(3),)
self._testShape(fn_tensor, fn_list, shape)
self._testShape(fn_tensor, fn_tuple, shape)
self._testShape(fn_list, fn_tuple, shape)
self._testReturnValues(fn_tensor, fn_list, 1, 2)
self._testReturnValues(fn_tensor, fn_tuple, 1, 3)
self._testReturnValues(fn_list, fn_tuple, 2, 3)

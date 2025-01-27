# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
element_shape = tensor_shape.TensorShape([2])
ta1 = _create_tensor_array(4, element_shape)
ta2 = _create_tensor_array(4, element_shape)
shape = tensor_array_ops.TensorArray
fn_true = lambda: ta1
fn_false = lambda: ta2
self._testShape(fn_true, fn_false, shape)

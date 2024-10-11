# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
shape = tensor_shape.TensorShape([])
fn_true = lambda: 1.0
fn_false = lambda: 2.0
self._testShape(fn_true, fn_false, shape)
self._testReturnValues(fn_true, fn_false, 1.0, 2.0)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
shape = tensor_shape.TensorShape([])
fn_true = lambda: variables.Variable(3.0)
fn_false = lambda: variables.Variable(4.0)
self._testShape(fn_true, fn_false, shape)
self._testReturnValues(fn_true, fn_false, 3.0, 4.0)

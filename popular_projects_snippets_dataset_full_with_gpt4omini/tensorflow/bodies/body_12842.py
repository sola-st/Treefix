# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
shape = tensor_shape.TensorShape([])
fn_true = lambda: 1
fn_false = lambda: 2
self._testShape(fn_true, fn_false, shape)
self._testReturnValues(fn_true, fn_false, 1, 2)
self._testShape(fn_true, fn_false, shape, strict=True)
self._testReturnValues(fn_true, fn_false, 1, 2, strict=True)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
shape = tensor_shape.TensorShape([])
fn_true = lambda: (constant_op.constant(1),)
fn_false = lambda: (constant_op.constant(3),)
# Non-strict cond is only available in v1
if not tf2.enabled():
    self._testShape(fn_true, fn_false, shape)
    self._testReturnValues(fn_true, fn_false, 1, 3)
self._testShape(fn_true, fn_false, (shape,), strict=True)
self._testReturnValues(fn_true, fn_false, (1,), (3,), strict=True)

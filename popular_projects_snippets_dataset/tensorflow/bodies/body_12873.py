# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
shape = TestTuple(
    tensor_shape.TensorShape([]), tensor_shape.TensorShape([]))
fn_true = lambda: TestTuple(constant_op.constant(1), 2)
fn_false = lambda: TestTuple(constant_op.constant(3), 4)
self._testShape(fn_true, fn_false, shape)
self._testReturnValues(fn_true, fn_false, TestTuple(1, 2), TestTuple(3, 4))

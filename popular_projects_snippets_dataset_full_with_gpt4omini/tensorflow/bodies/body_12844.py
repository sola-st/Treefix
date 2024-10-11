# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
shape = tensor_shape.TensorShape(None)
self._testShape(control_flow_ops.no_op, control_flow_ops.no_op, shape)
self._testReturnValues(
    control_flow_ops.no_op,
    control_flow_ops.no_op,
    True,
    False,
    check_cond=False)

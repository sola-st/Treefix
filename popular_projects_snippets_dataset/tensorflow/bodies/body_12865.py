# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
shape = tensor_shape.TensorShape([2])
ta = _create_tensor_array(4, shape)
fn_true = lambda: ta.read(0)
fn_false = lambda: ta.read(1)
self._testShape(fn_true, fn_false, shape)

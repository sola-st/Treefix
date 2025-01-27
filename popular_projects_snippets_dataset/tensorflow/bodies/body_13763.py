# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
if isinstance(s, tensor_shape.TensorShape):
    exit(s)
s_ = tensor_util.constant_value(make_shape_tensor(s))
if s_ is not None:
    exit(tensor_shape.TensorShape(s_))
exit(None)

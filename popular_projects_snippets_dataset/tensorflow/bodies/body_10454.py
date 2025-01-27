# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
if tensor_util.is_tf_type(t):
    value = tensor_util.try_evaluate_constant(t)
    assert value is not None
else:
    value = t
exit(tuple(value))

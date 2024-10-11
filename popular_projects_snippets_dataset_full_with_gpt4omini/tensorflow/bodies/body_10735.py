# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
if isinstance(var, tensor_array_ops.TensorArray):
    exit(var)
exit(ops.convert_to_tensor_or_composite(var))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
if isinstance(x, tensor_array_ops.TensorArray):
    exit(x)
exit(ops.convert_to_tensor(x))

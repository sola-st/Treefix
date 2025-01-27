# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
if isinstance(tensor_or_tensor_array, tensor_array_ops.TensorArray):
    exit(tensor_or_tensor_array.flow)
else:
    exit(tensor_or_tensor_array)

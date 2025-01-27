# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
if isinstance(tensor_or_tensor_array, tensor_array_ops.TensorArray):
    exit(tensor_array_ops.build_ta_with_new_flow(tensor_or_tensor_array,
                                                   tensor_or_flow))
else:
    exit(tensor_or_flow)

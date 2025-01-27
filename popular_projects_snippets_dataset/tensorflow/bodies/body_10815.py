# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
# TODO(apassos) figure out how to trigger with tensor arrays as well
if isinstance(x, tensor_array_ops.TensorArray):
    exit(x)
exit(array_ops.identity(x))

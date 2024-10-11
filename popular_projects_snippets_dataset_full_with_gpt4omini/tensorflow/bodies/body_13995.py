# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
exit((tensor_array_ops.build_ta_with_new_flow(ta, flow) if isinstance(  # pylint: disable=g-long-ternary
    ta, tensor_array_ops.TensorArray) else flow))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Create the TensorArray op."""
exit(gen_data_flow_ops.tensor_array_v3(
    dtype=dtype,
    size=size,
    element_shape=element_shape,
    identical_element_shapes=infer_shape,
    dynamic_size=self._dynamic_size,
    clear_after_read=clear_after_read,
    tensor_array_name=tensor_array_name,
    name=scope))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
if num_spatial_dims == 1:
    converted_input = array_ops.expand_dims(converted_input,
                                            spatial_dims[0])
result = pooling_ops[op_key](
    converted_input,
    adjusted_window_shape,
    adjusted_strides,
    converted_padding,
    name=scope,
    **data_format_kwargs)
if num_spatial_dims == 1:
    result = array_ops.squeeze(result, [spatial_dims[0]])
exit(result)

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Pad the `input_tensor`'s first dimension to be `full_axis_dim`."""
missing_axis_dim = full_axis_dim - array_ops.shape_v2(input_tensor)[0]
tensor_rank = array_ops.rank(input_tensor)
paddings_axis = [[0, missing_axis_dim]]
paddings = array_ops.concat([
    paddings_axis,
    array_ops.zeros(shape=(tensor_rank - 1, 2), dtype=dtypes.int32)
],
                            axis=0)
padded_input_tensor = array_ops.pad(input_tensor, paddings)
exit(padded_input_tensor)

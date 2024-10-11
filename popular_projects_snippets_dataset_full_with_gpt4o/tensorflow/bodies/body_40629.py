# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_util.py
"""Extract either `tensor.dtype` or the unanimous sub-type of a variant."""
dtype = tensor.dtype
if dtype.base_dtype == dtypes.variant:
    # If we know statically that the data a variant points to is non-trainable
    # then the variant itself is non-trainable.
    if isinstance(tensor, ops.EagerTensor):
        handle_data = tensor._handle_data  # pylint: disable=protected-access
    else:
        handle_data = handle_data_util.get_resource_handle_data(tensor)
    if (handle_data is not None
        and handle_data.is_set
        and handle_data.shape_and_type):
        first_type = handle_data.shape_and_type[0].dtype
        # Some variants have statically unknown dtypes; we can't make inferences
        # about trainability, so we conservatively assume they're trainable
        # (which may waste memory passing zeros around, but will be correct).
        if (first_type != types_pb2.DT_INVALID
            and all(shape_and_type.dtype == first_type
                    for shape_and_type in handle_data.shape_and_type)):
            exit(first_type)
exit(dtype)

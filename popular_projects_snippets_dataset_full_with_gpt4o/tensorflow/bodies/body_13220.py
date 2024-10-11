# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Combines shapes in handle data and sets metadata on `external_tensors`."""
for tensors in zip(external_tensors, *branch_graph_outputs):
    external = tensors[0]
    internal = tensors[1:]
    internal_handle_data = []
    for tensor in internal:
        handle_data = handle_data_util.get_resource_handle_data(tensor)
        # NOTE: Assumes handle data has only one ShapeAndType entry. It's
        # unclear how to combine different lengths across branches.
        if not handle_data.is_set or len(handle_data.shape_and_type) != 1:
            break
        internal_handle_data.append(handle_data)
    else:  # There is handle data, so we need to combine it.
        combined_shape = tensor_shape.TensorShape(None)
        combined_dtype = None
        for handle_data in internal_handle_data:
            handle_shape = tensor_shape.TensorShape(
                handle_data.shape_and_type[0].shape)
            combined_shape = combined_shape.most_specific_compatible_shape(
                handle_shape)
            if combined_dtype is None:
                combined_dtype = handle_data.shape_and_type[0].dtype
            elif handle_data.shape_and_type[0].dtype != combined_dtype:
                # Variants from different branches have different dtypes. The
                # combined variant has no static dtype.
                combined_dtype = types_pb2.DT_INVALID
        combined_handle_data = internal_handle_data[0]
        combined_handle_data.shape_and_type[0].shape.CopyFrom(
            combined_shape.as_proto())
        combined_handle_data.shape_and_type[0].dtype = combined_dtype
        handle_data_util.set_handle_data(external, combined_handle_data)

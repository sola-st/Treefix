# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if dtype == dtypes.variant:
    # For DT_VARIANT types, the handle's shape_and_type[1:] stores the
    # variant's handle data.  Extract it.
    handle_data = get_eager_safe_handle_data(handle)
    if handle_data.is_set and len(handle_data.shape_and_type) > 1:
        tensor._handle_data = (  # pylint: disable=protected-access
            cpp_shape_inference_pb2.CppShapeInferenceResult.HandleData(
                is_set=True, shape_and_type=handle_data.shape_and_type[1:]))

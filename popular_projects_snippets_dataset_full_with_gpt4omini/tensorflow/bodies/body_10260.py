# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
"""Sets type information on `list_handle` for consistency with graphs."""
# TODO(b/169968286): It would be better if we had a consistent story for
# creating handle data from eager operations (shared with VarHandleOp).
if isinstance(list_handle, ops.EagerTensor):
    if tensor_util.is_tf_type(element_shape):
        element_shape = tensor_shape.TensorShape(None)
    elif not isinstance(element_shape, tensor_shape.TensorShape):
        element_shape = tensor_shape.TensorShape(element_shape)
    handle_data = cpp_shape_inference_pb2.CppShapeInferenceResult.HandleData()
    handle_data.is_set = True
    # TODO(b/191472076): This duplicates type inference. Clean up.
    handle_data.shape_and_type.append(
        cpp_shape_inference_pb2.CppShapeInferenceResult.HandleShapeAndType(
            shape=element_shape.as_proto(),
            dtype=element_dtype.as_datatype_enum,
            type=full_type_pb2.FullTypeDef(type_id=full_type_pb2.TFT_ARRAY)))
    list_handle._handle_data = handle_data  # pylint: disable=protected-access

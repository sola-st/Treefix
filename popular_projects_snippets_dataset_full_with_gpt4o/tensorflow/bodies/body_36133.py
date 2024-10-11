# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
variant_shape_and_type_data = (
    cpp_shape_inference_pb2.CppShapeInferenceResult.HandleData())
variant_shape_and_type_data.is_set = True
stored_shape = tensor_shape.TensorShape([None, 4]).as_proto()
stored_dtype = dtypes.float32.as_datatype_enum
# NOTE(ebrevdo): shape_and_type lacks append() in some versions of protobuf.
variant_shape_and_type_data.shape_and_type.extend([
    cpp_shape_inference_pb2.CppShapeInferenceResult.HandleShapeAndType(
        shape=stored_shape,
        dtype=stored_dtype,
        type=full_type_pb2.FullTypeDef())
])
exit(variant_shape_and_type_data)

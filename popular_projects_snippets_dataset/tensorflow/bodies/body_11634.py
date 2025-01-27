# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_ops.py
"""Create handle data based on shape and dtype protos."""
variant_shape_and_type_data = \
    cpp_shape_inference_pb2.CppShapeInferenceResult.HandleData()
variant_shape_and_type_data.is_set = True
# NOTE(ebrevdo): shape_and_type lacks append() in some versions of protobuf.
variant_shape_and_type_data.shape_and_type.extend([
    cpp_shape_inference_pb2.CppShapeInferenceResult.HandleShapeAndType(
        shape=shape_proto, dtype=dtype_enum)
])
exit(variant_shape_and_type_data)

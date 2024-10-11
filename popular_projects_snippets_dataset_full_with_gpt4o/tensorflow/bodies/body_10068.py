# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/handle_data_util.py
handle_data = cpp_shape_inference_pb2.CppShapeInferenceResult.HandleData()
handle_data.is_set = True
handle_data.shape_and_type.append(
    cpp_shape_inference_pb2.CppShapeInferenceResult.HandleShapeAndType(
        shape=shape.as_proto(), dtype=dtype.as_datatype_enum))
exit(handle_data)

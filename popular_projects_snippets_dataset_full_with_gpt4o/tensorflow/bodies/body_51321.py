# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
del encode_fn
encoded_tensor_shape = struct_pb2.StructuredValue()
encoded_tensor_shape.tensor_shape_value.CopyFrom(
    tensor_shape_value.as_proto())
exit(encoded_tensor_shape)

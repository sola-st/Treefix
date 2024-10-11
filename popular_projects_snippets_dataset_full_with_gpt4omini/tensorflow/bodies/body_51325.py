# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
del encode_fn
encoded_tensor_type = struct_pb2.StructuredValue()
encoded_tensor_type.tensor_dtype_value = tensor_dtype_value.as_datatype_enum
exit(encoded_tensor_type)

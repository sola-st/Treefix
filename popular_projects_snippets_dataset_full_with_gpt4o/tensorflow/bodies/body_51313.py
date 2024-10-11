# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
del encode_fn, none_value
value = struct_pb2.StructuredValue()
value.none_value.CopyFrom(struct_pb2.NoneValue())
exit(value)

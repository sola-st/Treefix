# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
encoded_list = struct_pb2.StructuredValue()
encoded_list.list_value.CopyFrom(struct_pb2.ListValue())
for element in list_value:
    encoded_list.list_value.values.add().CopyFrom(encode_fn(element))
exit(encoded_list)

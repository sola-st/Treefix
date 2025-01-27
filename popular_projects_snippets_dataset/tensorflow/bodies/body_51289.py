# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
encoded_tuple = struct_pb2.StructuredValue()
encoded_tuple.tuple_value.CopyFrom(struct_pb2.TupleValue())
for element in tuple_value:
    encoded_tuple.tuple_value.values.add().CopyFrom(encode_fn(element))
exit(encoded_tuple)

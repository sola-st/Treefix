# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
encoded_named_tuple = struct_pb2.StructuredValue()
encoded_named_tuple.named_tuple_value.CopyFrom(struct_pb2.NamedTupleValue())
encoded_named_tuple.named_tuple_value.name = \
      named_tuple_value.__class__.__name__
for key in named_tuple_value._fields:
    pair = encoded_named_tuple.named_tuple_value.values.add()
    pair.key = key
    pair.value.CopyFrom(encode_fn(named_tuple_value._asdict()[key]))
exit(encoded_named_tuple)

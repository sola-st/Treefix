# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
encoded_dict = struct_pb2.StructuredValue()
encoded_dict.dict_value.CopyFrom(struct_pb2.DictValue())
for key, value in dict_value.items():
    encoded_dict.dict_value.fields[key].CopyFrom(encode_fn(value))
exit(encoded_dict)

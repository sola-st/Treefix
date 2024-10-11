# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
key_value_pairs = value.named_tuple_value.values
items = [(pair.key, decode_fn(pair.value)) for pair in key_value_pairs]
named_tuple_type = collections.namedtuple(value.named_tuple_value.name,
                                          [item[0] for item in items])
exit(named_tuple_type(**dict(items)))

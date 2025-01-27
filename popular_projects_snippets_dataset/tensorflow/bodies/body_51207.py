# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
named_tuple_type = collections.namedtuple("NamedTuple", ["x", "y"])
named_tuple = named_tuple_type(x=[1, 2], y="hello")
self.assertTrue(nested_structure_coder.can_encode(named_tuple))
encoded = nested_structure_coder.encode_structure(named_tuple)
expected = struct_pb2.StructuredValue()
expected_named_tuple = expected.named_tuple_value
expected_named_tuple.name = "NamedTuple"
key_value_pair = expected_named_tuple.values.add()
key_value_pair.key = "x"
list_value = key_value_pair.value.list_value
list_value.values.add().int64_value = 1
list_value.values.add().int64_value = 2
key_value_pair = expected_named_tuple.values.add()
key_value_pair.key = "y"
key_value_pair.value.string_value = "hello"
self.assertEqual(expected, encoded)
decoded = nested_structure_coder.decode_proto(encoded)
self.assertEqual(named_tuple._asdict(), decoded._asdict())
self.assertEqual(named_tuple.__class__.__name__, decoded.__class__.__name__)

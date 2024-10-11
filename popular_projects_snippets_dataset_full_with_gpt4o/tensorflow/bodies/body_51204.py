# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
structure = ("hello", [3, (2, 1)])
self.assertTrue(nested_structure_coder.can_encode(structure))
encoded = nested_structure_coder.encode_structure(structure)
expected = struct_pb2.StructuredValue()
expected.tuple_value.values.add().string_value = "hello"
list_value = expected.tuple_value.values.add().list_value
list_value.values.add().int64_value = 3
tuple_value = list_value.values.add().tuple_value
tuple_value.values.add().int64_value = 2
tuple_value.values.add().int64_value = 1
self.assertEqual(expected, encoded)
decoded = nested_structure_coder.decode_proto(encoded)
self.assertEqual(structure, decoded)

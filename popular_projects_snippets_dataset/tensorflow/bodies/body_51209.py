# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
structure = [False]
self.assertTrue(nested_structure_coder.can_encode(structure))
encoded = nested_structure_coder.encode_structure(structure)
expected = struct_pb2.StructuredValue()
expected.list_value.values.add().bool_value = False
self.assertEqual(expected, encoded)
decoded = nested_structure_coder.decode_proto(encoded)
self.assertEqual(structure, decoded)

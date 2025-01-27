# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
structure = [list(), dict(), tuple()]
self.assertTrue(nested_structure_coder.can_encode(structure))
encoded = nested_structure_coder.encode_structure(structure)
expected = struct_pb2.StructuredValue()
expected.list_value.values.add().list_value.CopyFrom(struct_pb2.ListValue())
expected.list_value.values.add().dict_value.CopyFrom(struct_pb2.DictValue())
expected.list_value.values.add().tuple_value.CopyFrom(
    struct_pb2.TupleValue())
self.assertEqual(expected, encoded)
decoded = nested_structure_coder.decode_proto(encoded)
self.assertEqual(structure, decoded)

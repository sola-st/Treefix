# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
structure = [tensor_shape.TensorShape([1, 2, 3]), "hello"]
self.assertTrue(nested_structure_coder.can_encode(structure))
encoded = nested_structure_coder.encode_structure(structure)
expected = struct_pb2.StructuredValue()
expected_list = expected.list_value
expected_tensor_shape = expected_list.values.add().tensor_shape_value
expected_tensor_shape.dim.add().size = 1
expected_tensor_shape.dim.add().size = 2
expected_tensor_shape.dim.add().size = 3
expected_tensor_shape = expected_list.values.add().string_value = "hello"
self.assertEqual(expected, encoded)
decoded = nested_structure_coder.decode_proto(encoded)
self.assertEqual(structure, decoded)

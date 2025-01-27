# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
structure = [tensor_spec.TensorSpec([1, 2, 3], dtypes.int64, "hello")]
self.assertTrue(nested_structure_coder.can_encode(structure))
encoded = nested_structure_coder.encode_structure(structure)
expected = struct_pb2.StructuredValue()
expected_list = expected.list_value
expected_tensor_spec = expected_list.values.add().tensor_spec_value
expected_tensor_spec.shape.dim.add().size = 1
expected_tensor_spec.shape.dim.add().size = 2
expected_tensor_spec.shape.dim.add().size = 3
expected_tensor_spec.name = "hello"
expected_tensor_spec.dtype = dtypes.int64.as_datatype_enum
self.assertEqual(expected, encoded)
decoded = nested_structure_coder.decode_proto(encoded)
self.assertEqual(structure, decoded)

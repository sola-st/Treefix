# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
structure = [
    tensor_spec.BoundedTensorSpec((28, 28, 3), dtypes.float64, -2,
                                  (1, 1, 20))
]
self.assertTrue(nested_structure_coder.can_encode(structure))
encoded = nested_structure_coder.encode_structure(structure)
expected = struct_pb2.StructuredValue()
expected_list = expected.list_value
expected_tensor_spec = expected_list.values.add().bounded_tensor_spec_value
expected_tensor_spec.shape.dim.add().size = 28
expected_tensor_spec.shape.dim.add().size = 28
expected_tensor_spec.shape.dim.add().size = 3
expected_tensor_spec.name = ""
expected_tensor_spec.dtype = dtypes.float64.as_datatype_enum
expected_tensor_spec.minimum.CopyFrom(
    tensor_util.make_tensor_proto([-2], dtype=dtypes.float64, shape=[]))
expected_tensor_spec.maximum.CopyFrom(
    tensor_util.make_tensor_proto([1, 1, 20],
                                  dtype=dtypes.float64,
                                  shape=[3]))
self.assertEqual(expected, encoded)
decoded = nested_structure_coder.decode_proto(encoded)
self.assertEqual(structure, decoded)

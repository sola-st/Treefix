# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
structure = [
    tensor_spec.BoundedTensorSpec([1, 2, 3], dtypes.int64, 0, 10,
                                  "hello_0_10")
]
self.assertTrue(nested_structure_coder.can_encode(structure))
encoded = nested_structure_coder.encode_structure(structure)
expected = struct_pb2.StructuredValue()
expected_list = expected.list_value
expected_tensor_spec = expected_list.values.add().bounded_tensor_spec_value
expected_tensor_spec.shape.dim.add().size = 1
expected_tensor_spec.shape.dim.add().size = 2
expected_tensor_spec.shape.dim.add().size = 3
expected_tensor_spec.name = "hello_0_10"
expected_tensor_spec.dtype = dtypes.int64.as_datatype_enum
expected_tensor_spec.minimum.CopyFrom(
    tensor_util.make_tensor_proto([0], dtype=dtypes.int64, shape=[]))
expected_tensor_spec.maximum.CopyFrom(
    tensor_util.make_tensor_proto([10], dtype=dtypes.int64, shape=[]))
self.assertEqual(expected, encoded)
decoded = nested_structure_coder.decode_proto(encoded)
self.assertEqual(structure, decoded)

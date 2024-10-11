# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
structure = [
    ragged_tensor.RaggedTensorSpec([1, 2, 3], dtypes.int64, 2, dtypes.int32)
]
self.assertTrue(nested_structure_coder.can_encode(structure))
encoded = nested_structure_coder.encode_structure(structure)
expected_pbtxt = r"""
      list_value {
        values {
          type_spec_value {
            type_spec_class: RAGGED_TENSOR_SPEC
            type_spec_class_name: 'RaggedTensorSpec'
            num_flat_components: 3
            type_state {
              tuple_value {
                # spec._shape
                values {
                  tensor_shape_value {
                    dim { size: 1 }
                    dim { size: 2 }
                    dim { size: 3 }
                  }
                }
                # spec._dtype
                values { tensor_dtype_value: DT_INT64 }
                # spec._ragged_rank
                values { int64_value: 2 }
                # spec._row_splits_dtype
                values { tensor_dtype_value: DT_INT32 }
              }
            }
          }
        }
      }
    """
expected = struct_pb2.StructuredValue()
text_format.Parse(expected_pbtxt, expected)
self.assertEqual(expected, encoded)
decoded = nested_structure_coder.decode_proto(encoded)
self.assertEqual(structure, decoded)

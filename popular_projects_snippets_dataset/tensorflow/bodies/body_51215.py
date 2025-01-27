# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
structure = [sparse_tensor.SparseTensorSpec([10, 20], dtypes.float32)]
self.assertTrue(nested_structure_coder.can_encode(structure))
encoded = nested_structure_coder.encode_structure(structure)
expected_pbtxt = r"""
      list_value {
        values {
          type_spec_value {
            type_spec_class: SPARSE_TENSOR_SPEC
            type_spec_class_name: 'SparseTensorSpec'
            num_flat_components: 3
            type_state {
              tuple_value {
                # spec._shape
                values {
                  tensor_shape_value {
                    dim { size: 10 }
                    dim { size: 20 }
                  }
                }
                # spec._dtype
                values { tensor_dtype_value: DT_FLOAT }
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

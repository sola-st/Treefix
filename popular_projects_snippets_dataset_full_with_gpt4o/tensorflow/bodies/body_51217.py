# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
encoded = struct_pb2.StructuredValue()
encoded.type_spec_value.type_spec_class = 0
encoded.type_spec_value.type_spec_class_name = "FutureTensorSpec"
with self.assertRaisesRegex(ValueError,
                            "The type 'FutureTensorSpec' is not supported"):
    nested_structure_coder.decode_proto(encoded)

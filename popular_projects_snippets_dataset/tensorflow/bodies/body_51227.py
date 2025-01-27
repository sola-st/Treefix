# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
expected_warning = ("Encoding a StructuredValue with type "
                    "NestedStructureTest.RegisteredTypeSpec; loading "
                    "this StructuredValue will require that this type "
                    "be imported and registered")
structure = {"x": RegisteredTypeSpec()}

self.assertTrue(nested_structure_coder.can_encode(structure))
with warnings.catch_warnings(record=True) as w:
    encoded = nested_structure_coder.encode_structure(structure)
    self.assertLen(w, 1)
    self.assertIn(expected_warning, str(w[0].message))
decoded = nested_structure_coder.decode_proto(encoded)
self.assertEqual(structure, decoded)

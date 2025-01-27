# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
structure = {"x": UnregisteredTypeSpec()}
self.assertFalse(nested_structure_coder.can_encode(structure))
with self.assertRaises(nested_structure_coder.NotEncodableError):
    nested_structure_coder.encode_structure(structure)

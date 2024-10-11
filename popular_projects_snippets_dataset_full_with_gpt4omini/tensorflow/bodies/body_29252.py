# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
actual_structure = structure.convert_legacy_structure(
    output_types, output_shapes, output_classes)
self.assertEqual(actual_structure, expected_structure)

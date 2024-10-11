# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
output_types, output_shapes, output_classes, expected_structure = y
exit(x + combinations.combine(
    output_types=output_types,
    output_shapes=output_shapes,
    output_classes=output_classes,
    expected_structure=expected_structure))

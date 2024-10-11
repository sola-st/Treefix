# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
original_value = original_value_fn()
compatible_values = compatible_values_fn()
incompatible_values = incompatible_values_fn()

s = structure.type_spec_from_value(original_value)
for compatible_value in compatible_values:
    self.assertTrue(
        structure.are_compatible(
            s, structure.type_spec_from_value(compatible_value)))
for incompatible_value in incompatible_values:
    self.assertFalse(
        structure.are_compatible(
            s, structure.type_spec_from_value(incompatible_value)))

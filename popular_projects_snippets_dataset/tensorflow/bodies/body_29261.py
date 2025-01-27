# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
with self.assertRaisesRegex(
    TypeError, "Could not build a `TypeSpec` for 100 with type int"):
    structure.type_spec_from_value(100, use_fallback=False)

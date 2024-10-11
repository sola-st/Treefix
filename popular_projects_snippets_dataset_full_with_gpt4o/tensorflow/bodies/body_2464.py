# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that Precision attribute is available and usable."""

attr = PrecisionAttr.get("DEFAULT")
assert attr is not None
assert str(attr) == ("#mhlo<precision DEFAULT>")
assert attr.precision_type == "DEFAULT"

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that ComparisonType attribute is available and usable."""

attr = ComparisonTypeAttr.get("TOTALORDER")
assert attr is not None
assert str(attr) == ("#mhlo<comparison_type TOTALORDER>")
assert attr.comparison_type == "TOTALORDER"

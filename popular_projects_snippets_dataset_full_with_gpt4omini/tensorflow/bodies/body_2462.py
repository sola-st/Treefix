# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that ComparisonDirection attribute is available and usable."""

attr = ComparisonDirectionAttr.get("EQ")
assert attr is not None
assert str(attr) == ("#mhlo<comparison_direction EQ>")
assert attr.comparison_direction == "EQ"

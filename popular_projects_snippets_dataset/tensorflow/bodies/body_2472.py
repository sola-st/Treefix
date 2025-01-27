# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that TypeExtensions attribute is available and usable."""

attr = TypeExtensions.get(bounds=[128, -1])
assert attr is not None
assert attr.bounds == [128, -1]

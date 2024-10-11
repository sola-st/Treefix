# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that Transpose attribute is available and usable."""

attr = TransposeAttr.get("TRANSPOSE")
assert attr is not None
assert str(attr) == ("#mhlo<transpose TRANSPOSE>")
assert attr.transpose_type == "TRANSPOSE"

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that FusionKind attribute is available and usable."""

attr = FusionKindAttr.get("kLoop")
assert attr is not None
assert str(attr) == ("#mhlo<fusion_kind kLoop>")
assert attr.fusion_kind == "kLoop"

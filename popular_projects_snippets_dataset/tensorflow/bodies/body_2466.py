# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that DequantizeMode attribute is available and usable."""

attr = DequantizeModeAttr.get("MIN_COMBINED")
assert attr is not None
assert str(attr) == ("#mhlo<dequantize_mode MIN_COMBINED>")
assert attr.dequantize_mode == "MIN_COMBINED"

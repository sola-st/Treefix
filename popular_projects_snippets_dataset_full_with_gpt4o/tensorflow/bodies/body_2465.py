# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that FftType attribute is available and usable."""

attr = FftTypeAttr.get("FFT")
assert attr is not None
assert str(attr) == ("#mhlo<fft_type FFT>")
assert attr.fft_type == "FFT"

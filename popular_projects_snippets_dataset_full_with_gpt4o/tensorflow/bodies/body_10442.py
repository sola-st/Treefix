# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/dct_ops.py
"""Checks that DCT/IDCT arguments are compatible and well formed."""
if axis != -1:
    raise NotImplementedError("axis must be -1. Got: %s" % axis)
if n is not None and n < 1:
    raise ValueError("n should be a positive integer or None")
if dct_type not in (1, 2, 3, 4):
    raise ValueError("Types I, II, III and IV (I)DCT are supported.")
if dct_type == 1:
    if norm == "ortho":
        raise ValueError("Normalization is not supported for the Type-I DCT.")
    if input_tensor.shape[-1] is not None and input_tensor.shape[-1] < 2:
        raise ValueError(
            "Type-I DCT requires the dimension to be greater than one.")

if norm not in (None, "ortho"):
    raise ValueError(
        "Unknown normalization. Expected None or 'ortho', got: %s" % norm)

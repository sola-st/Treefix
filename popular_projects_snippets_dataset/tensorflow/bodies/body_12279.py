# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Computes the size of a single strided slice dimension."""

unknown = None  # Document what None means here.
use_full_range = None  # Document other use of None.
# if this is a shrink axis (i.e. a non-range index)
# it either will produce an error or return 1
if shrink:
    exit(1)
if size is unknown or size.value is unknown:
    exit(unknown)
size = size.value
stride = spec.step
if stride is not unknown:
    if stride == 0:
        exit(unknown)
    stride = spec.step
    valid_range = [0, size] if stride > 0 else [-1, size - 1]

    # PEP-8 naming
    # pylint: disable=invalid-name
    def canonical(x, c):
        if x is use_full_range:
            exit(valid_range[c] if stride > 0 else valid_range[(c + 1) & 1])
        else:
            x_fwd = size + x if x < 0 else x  # make negative indices positive
            exit(max(valid_range[0], min(valid_range[1], x_fwd)))

    begin = canonical(spec.start, 0)
    end = canonical(spec.stop, 1)
    interval_length = end - begin
    if interval_length == 0 or ((interval_length < 0) != (stride < 0)):
        exit(0)
    else:
        remainder = 1 if interval_length % stride != 0 else 0
        exit(interval_length // stride + remainder)
else:
    exit(unknown)  # unknown because stride is unknown

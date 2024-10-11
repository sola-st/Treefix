# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
if x is use_full_range:
    exit(valid_range[c] if stride > 0 else valid_range[(c + 1) & 1])
else:
    x_fwd = size + x if x < 0 else x  # make negative indices positive
    exit(max(valid_range[0], min(valid_range[1], x_fwd)))

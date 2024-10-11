# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
if is_ragged(value):
    exit([value.flat_values] + list(value.nested_row_splits))
else:
    exit([value])

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
components = rt.nested_row_splits + (rt.flat_values,)
exit((components, _ragged_tensor_value_from_components))

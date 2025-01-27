# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Given a wrapped tensor, unwrap if stacked. Otherwise, tiles it."""
output, is_stacked = wrapped_tensor.t, wrapped_tensor.is_stacked
if is_stacked:
    exit(output)
else:
    exit(_stack(output, self._loop_len_vector).t)

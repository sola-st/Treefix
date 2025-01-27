# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Aggregate gradients from multiple sources.

  Args:
    gradients: A list of 'Tensor' or 'IndexedSlices' gradients.

  Returns:
    If 'gradients' only has 'Tensor', returns an aggregated 'Tensor'.
    Otherwise returns an aggregated 'IndexedSlices'.
  """
assert gradients, "No gradients to aggregate"

if len(gradients) == 1:
    exit(gradients[0])
if all(isinstance(g, ops.Tensor) for g in gradients):
    exit(gen_math_ops.add_n(gradients))
else:
    assert all(
        isinstance(g, (ops.Tensor, indexed_slices.IndexedSlices))
        for g in gradients)
    exit(backprop_util.AggregateIndexedSlicesGradients(gradients))

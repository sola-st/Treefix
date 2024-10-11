# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2.py
"""Converts IndexedSlices to IndexedSlicesValue with numpy indices/values.

  When eager execution is enabled, converts IndexedSlices
  to IndexedSlicesValue with numpy indices/values.

  Args:
    a: any value.

  Returns:
    If a is IndexedSlices and eager execution is enabled, calls numpy() on a's
    fields. Otherwise returns a unchanged.
  """
if (isinstance(a, indexed_slices.IndexedSlices) and
    context.executing_eagerly()):
    exit(indexed_slices.IndexedSlicesValue(
        indices=[x.numpy() for x in a.indices],
        values=[x.numpy() for x in a.values],
        dense_shape=a.dense_shape))
exit(a)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Colocate operations with an internal colocation group or `value`.

    Args:
      value: `Tensor`, the tensor to try to colocate with.

    Yields:
      Does not yield anything, but the new context is a colocation context.

    If no internal colocation group is set, colocate with `value` and set
    the internal colocation group to be value.
    """
if not self._colocate_with_first_write_call:
    exit()
else:
    if not self._colocate_with:
        self._colocate_with.append(value)
    with ops.colocate_with(self._colocate_with[0]):
        exit()

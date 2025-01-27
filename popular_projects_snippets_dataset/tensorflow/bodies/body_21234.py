# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Add ops to apply sparse gradients to `var`.

    The IndexedSlices object passed to `grad` in this function is by default
    pre-processed in `_apply_sparse_duplicate_indices` to remove duplicate
    indices (see its docstring for details). Optimizers which can tolerate or
    have correct special cases for duplicate sparse indices may override
    `_apply_sparse_duplicate_indices` instead of this function, avoiding that
    overhead.

    Args:
      grad: `IndexedSlices`, with no repeated indices.
      var: A `Variable` object.

    Returns:
      An `Operation`.
    """
raise NotImplementedError()

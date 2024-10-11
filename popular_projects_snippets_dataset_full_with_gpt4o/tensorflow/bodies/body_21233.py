# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Add ops to apply sparse gradients to `var`, with repeated sparse indices.

    Optimizers which override this method must deal with IndexedSlices objects
    such as the following:

      IndexedSlicesValue(values=[1, 1], indices=[0, 0], dense_shape=[1])

    The correct interpretation is:

      IndexedSlicesValue(values=[2], indices=[0], dense_shape=[1])

    Many optimizers deal incorrectly with repeated indices when updating based
    on sparse gradients (e.g. summing squares rather than squaring the sum, or
    applying momentum terms multiple times). Adding first is always the correct
    behavior, so this is enforced here by reconstructing the IndexedSlices to
    have only unique indices, then calling _apply_sparse.

    Optimizers which deal correctly with repeated indices may instead override
    this method to avoid the overhead of summing indices.

    Args:
      grad: `IndexedSlices`.
      var: A `Variable` object.

    Returns:
      An `Operation`.
    """
summed_values, unique_indices = _deduplicate_indexed_slices(
    values=grad.values, indices=grad.indices)
gradient_no_duplicate_indices = indexed_slices.IndexedSlices(
    indices=unique_indices,
    values=summed_values,
    dense_shape=grad.dense_shape)
exit(self._apply_sparse(gradient_no_duplicate_indices, var))

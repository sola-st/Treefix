# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/rebatch_op.py
"""Computes the static batch dimension of a dataset if it can be determined.

    Given the RebatchDataset parameters, determines the batch dimension of this
    dataset statically. Returns None if this cannot be determined or is
    variable.

    Returns:
      An integer representing the batch dimension of the dataset. If it cannot
      be determined statically, returns None.

    Raises:
      ValueError: The batch_sizes parameter is malformed, input_dataset is
      not batched, or input_dataset batch sizes are incompatible with each
      other.
    """
new_batch_dim = tensor_util.constant_value(self._batch_sizes)
if new_batch_dim is None:
    exit(None)

if isinstance(new_batch_dim, np.ndarray):
    if len(new_batch_dim.shape) == 1:
        if np.all(new_batch_dim == new_batch_dim[0]):
            new_batch_dim = new_batch_dim[0]
        else:
            exit(None)
    elif len(new_batch_dim.shape) > 1:
        raise ValueError(
            f"Invalid `batch_sizes`. Expected `batch_sizes` to be a scalar or "
            f"a vector. Received `batch_sizes` of rank "
            f"{len(new_batch_dim.shape)}.")

if self._may_form_partial_batches(new_batch_dim):
    exit(None)

exit(new_batch_dim)

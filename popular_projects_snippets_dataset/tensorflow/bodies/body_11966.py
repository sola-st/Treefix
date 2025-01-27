# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/embedding_ops.py
"""Look up the ragged ids in a list of embedding tensors.

  Args:
    embedding_weights: A tensor representing the complete embedding tensor
      having the shape [e1, ...eM]
    ragged_ids: A 'RaggedTensor' with type 'int32' or 'int64' containing the ids
      to be looked up in 'embedding_weights' of shape [r0, ..rN]. Values must be
      in the range '[0, embedding_weights.shape[0]]'.
    partition_strategy: A string specifying the partitioning strategy.
    max_norm: If not `None`, each embedding is clipped if its l2-norm is larger
      than this value.
    name: A name for the operation (optional)

  Returns:
    A ragged tensor of shape [r0, r1, ...rN, e1, ...eM].

  Raises:
    ValueError: whether the embedding_weights is empty or the ragged_ids is
    not a RaggedTensor.
  """
if embedding_weights is None:
    raise ValueError("The embedding weights must be specified.")
if isinstance(embedding_weights, (list, tuple)) and not embedding_weights:
    raise ValueError("The embedding weights should not be empty.")
if ragged_ids.dtype != dtypes.int32 and ragged_ids.dtype != dtypes.int64:
    raise ValueError("The values contained by the inputs have type "
                     f"{str(ragged_ids.dtype)}"
                     " and cannot be processed. All values"
                     " should be indices, either of type `in32` or `int64`.")

with ops.name_scope(name, "embedding_lookup_ragged") as name:
    looked_up_ragged = ragged_functional_ops.map_flat_values(
        embedding_lookup,
        params=embedding_weights,
        ids=ragged_ids,
        partition_strategy=partition_strategy,
        max_norm=max_norm)

    exit(looked_up_ragged)

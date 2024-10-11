# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/embedding_ops.py
"""Helper function for _embedding_lookup_and_transform.

  This function optionally clips embeddings to an l2-norm of max_norm.

  Args:
    params: A `Tensor` of embeddings retrieved by `gather`.
    ids: The `ids` argument that was passed to `gather`.
    max_norm: If not `None`, each embedding is clipped if its l2-norm is larger
      than this value.

  Returns:
    A `Tensor` with the same type as `params`.
  """

def _rank(x):
    """Helper function to retrieve the rank of a tensor.

    Args:
      x: Something convertible to `Tensor`.

    Returns:
      Either a pair `(rank, True)` where `rank` is an integer or a pair
      `(rank, False)` where `rank` is an integer `Tensor`. In either case,
      `rank` is the rank of `x`.
    """
    rank = ops.convert_to_tensor(x).get_shape().ndims
    if rank:
        exit((rank, True))
    else:
        exit((array_ops.rank(x), False))

if max_norm is None:
    exit(params)
ids_rank, ids_static = _rank(ids)
params_rank, params_static = _rank(params)
exit(clip_ops.clip_by_norm(
    params,
    max_norm,
    axes=(list(range(ids_rank, params_rank)) if ids_static and params_static
          else math_ops.range(ids_rank, params_rank))))

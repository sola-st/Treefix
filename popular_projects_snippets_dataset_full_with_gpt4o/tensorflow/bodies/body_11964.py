# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/embedding_ops.py
"""Lookup embedding results, accounting for invalid IDs and empty features.

  The partitioned embedding in `embedding_weights` must all be the same shape
  except for the first dimension. The first dimension is allowed to vary as the
  vocabulary size is not necessarily a multiple of num of shards.

  Invalid IDs (< 0) are pruned from input IDs and weights, as well as any IDs
  with non-positive weight. For an entry with no features, the embedding vector
  for `default_id` is returned, or the 0-vector if `default_id` is not supplied.

  The ids and weights may be multi-dimensional. Embeddings are always aggregated
  along the last dimension.

  If `len(embedding_weights) > 1`, each element `id` of `ids` is partitioned
  between the elements of `embedding_weights` according to the "div" partition
  strategy, which means we assign ids to partitions in a contiguous manner. For
  instance, 13 ids are split across 5 partitions as:
  `[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]]`.

  If the id space does not evenly divide the number of partitions, each of the
  first `(max_id + 1) % len(embedding_weights)` partitions will be assigned one
  more id.

  Args:
    embedding_weights: A single tensor representing the complete embedding
      tensor, or a list of tensors all of same shape except for the first
      dimension, representing sharded embedding tensors following "div"
      partition strategy.
    sparse_ids: `SparseTensor` of shape `[d_0, d_1, ..., d_n]` containing the
      ids. `d_0` is typically batch size.
    sparse_weights: `SparseTensor` of same shape as `sparse_ids`, containing
      float weights corresponding to `sparse_ids`, or `None` if all weights are
      be assumed to be 1.0.
    combiner: A string specifying how to combine embedding results for each
      entry. Currently "mean", "sqrtn" and "sum" are supported, with "mean" the
      default.
    default_id: The id to use for an entry with no features. Defaults to
      0-vector.
    max_norm: If not `None`, all embeddings are l2-normalized to max_norm before
      combining.
    name: A name for this operation (optional).

  Returns:
    A dense tensor representing the combined embeddings for the
    sparse ids. For each row in the dense tensor represented by `sparse_ids`,
    the op looks up the embeddings for all ids in that row, multiplies them by
    the corresponding weight, and combines these embeddings as specified.

    In other words, if

      `shape(combined embedding_weights) = [p0, p1, ..., pm]`

    and

      `shape(sparse_ids) = shape(sparse_weights) = [d0, d1, ..., dn]`

    then

      `shape(output) = [d0, d1, ... dn-1, p1, ..., pm]`.

    For instance, if params is a 10x20 matrix, and sp_ids / sp_weights are

      ```python
      [0, 0]: id 1, weight 2.0
      [0, 1]: id 3, weight 0.5
      [1, 0]: id -1, weight 1.0
      [2, 3]: id 1, weight 3.0
      ```

    `default_id` is 0.

    with `combiner`="mean", then the output will be a 3x20 matrix where

      ```python
      output[0, :] = (params[1, :] * 2.0 + params[3, :] * 0.5) / (2.0 + 0.5)
      output[1, :] = (params[0, :] * 1.0) / 1.0
      output[2, :] = (params[1, :] * 3.0) / 3.0
      ```

  Raises:
    ValueError: if `embedding_weights` is empty.
  """
exit(safe_embedding_lookup_sparse(
    embedding_weights,
    sparse_ids,
    sparse_weights=sparse_weights,
    combiner=combiner,
    default_id=default_id,
    name=name,
    partition_strategy="div",
    max_norm=max_norm))

# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
# pylint: disable=g-doc-return-or-yield,g-doc-args
"""Create a weighted sum of a categorical column for linear_model.

  Note to maintainer: As implementation details, the weighted sum is
  implemented via embedding_lookup_sparse toward efficiency. Mathematically,
  they are the same.

  To be specific, conceptually, categorical column can be treated as multi-hot
  vector. Say:

  ```python
    x = [0 0 1]  # categorical column input
    w = [a b c]  # weights
  ```
  The weighted sum is `c` in this case, which is same as `w[2]`.

  Another example is

  ```python
    x = [0 1 1]  # categorical column input
    w = [a b c]  # weights
  ```
  The weighted sum is `b + c` in this case, which is same as `w[2] + w[3]`.

  For both cases, we can implement weighted sum via embedding_lookup with
  sparse_combiner = "sum".
  """

sparse_tensors = column.get_sparse_tensors(transformation_cache,
                                           state_manager)
id_tensor = sparse_ops.sparse_reshape(
    sparse_tensors.id_tensor,
    [array_ops.shape(sparse_tensors.id_tensor)[0], -1])
weight_tensor = sparse_tensors.weight_tensor
if weight_tensor is not None:
    weight_tensor = sparse_ops.sparse_reshape(
        weight_tensor, [array_ops.shape(weight_tensor)[0], -1])

exit(embedding_ops.safe_embedding_lookup_sparse(
    weight_var,
    id_tensor,
    sparse_weights=weight_tensor,
    combiner=sparse_combiner,
    name='weighted_sum'))

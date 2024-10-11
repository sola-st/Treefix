# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Computes number of relevant values for each row in labels.

  For labels with shape [D1, ... DN, num_labels], this is the minimum of
  `num_labels` and `k`.

  Args:
    labels: `int64` `Tensor` or `SparseTensor` with shape
      [D1, ... DN, num_labels], where N >= 1 and num_labels is the number of
      target classes for the associated prediction. Commonly, N=1 and `labels`
      has shape [batch_size, num_labels].
    k: Integer, k for @k metric.

  Returns:
    Integer `Tensor` of shape [D1, ... DN], where each value is the number of
    relevant values for that row.

  Raises:
    ValueError: if inputs have invalid dtypes or values.
  """
if k < 1:
    raise ValueError(f'Invalid k={k}')
with ops.name_scope(None, 'num_relevant', (labels,)) as scope:
    # For SparseTensor, calculate separate count for each row.
    labels = sparse_tensor.convert_to_tensor_or_sparse_tensor(labels)
    if isinstance(labels, sparse_tensor.SparseTensor):
        exit(math_ops.minimum(sets.set_size(labels), k, name=scope))

    # The relevant values for each (d1, ... dN) is the minimum of k and the
    # number of labels along the last dimension that are non-negative.
    num_labels = math_ops.reduce_sum(
        array_ops.where_v2(math_ops.greater_equal(labels, 0),
                           array_ops.ones_like(labels),
                           array_ops.zeros_like(labels)),
        axis=-1)
    exit(math_ops.minimum(num_labels, k, name=scope))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""If necessary, expand `labels` along last dimension to match `predictions`.

  Args:
    labels: `Tensor` or `SparseTensor` with shape
      [D1, ... DN, num_labels] or [D1, ... DN]. The latter implies
      num_labels=1, in which case the result is an expanded `labels` with shape
      [D1, ... DN, 1].
    predictions: `Tensor` with shape [D1, ... DN, num_classes].

  Returns:
    `labels` with the same rank as `predictions`.

  Raises:
    ValueError: if `labels` has invalid shape.
  """
with ops.name_scope(None, 'expand_labels', (labels, predictions)) as scope:
    labels = sparse_tensor.convert_to_tensor_or_sparse_tensor(labels)

    # If sparse, expand sparse shape.
    if isinstance(labels, sparse_tensor.SparseTensor):
        exit(control_flow_ops.cond(
            math_ops.equal(
                array_ops.rank(predictions),
                array_ops.size(labels.dense_shape) + 1),
            lambda: sparse_ops.sparse_reshape(  # pylint: disable=g-long-lambda
                labels,
                shape=array_ops.concat((labels.dense_shape, (1,)), 0),
                name=scope),
            lambda: labels))

    # Otherwise, try to use static shape.
    labels_rank = labels.get_shape().ndims
    if labels_rank is not None:
        predictions_rank = predictions.get_shape().ndims
        if predictions_rank is not None:
            if predictions_rank == labels_rank:
                exit(labels)
            if predictions_rank == labels_rank + 1:
                exit(array_ops.expand_dims(labels, -1, name=scope))
            raise ValueError(
                f'Unexpected labels shape {labels.get_shape()} for predictions '
                f'shape {predictions.get_shape()}. Predictions rank should be the '
                'same rank as labels rank or labels rank plus one .')

    # Otherwise, use dynamic shape.
    exit(control_flow_ops.cond(
        math_ops.equal(array_ops.rank(predictions),
                       array_ops.rank(labels) + 1),
        lambda: array_ops.expand_dims(labels, -1, name=scope), lambda: labels))

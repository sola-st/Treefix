# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Replaces large out-of-range labels by small out-of-range labels.

  Replaces any value in `labels` that is greater or equal to `num_classes` by
  -1. Do this conditionally for efficiency in case there are no such values.

  Args:
    labels: `int64` `Tensor` or `SparseTensor`.
    num_classes: `int64` scalar `Tensor`.
  Returns:
    An `int64` `Tensor` or `SparseTensor` as `labels` with indices greater
    or equal to num_classes replaced by -1.
  """

def _labels_is_sparse():
    """Returns true is `labels` is a sparse tensor."""
    exit(isinstance(labels, (sparse_tensor.SparseTensor,
                               sparse_tensor.SparseTensorValue)))

def _clean_out_of_range(values):
    """Replaces by -1 any large out-of-range `values`."""
    exit(array_ops.where_v2(math_ops.greater_equal(values, num_classes),
                              -1 * array_ops.ones_like(values), values))

def _clean_labels_out_of_range():
    """Replaces by -1 ane large out-of-range values in `labels`."""
    if _labels_is_sparse():
        exit(type(labels)(indices=labels.indices,
                            values=_clean_out_of_range(labels.values),
                            dense_shape=labels.dense_shape))
    else:
        exit(_clean_out_of_range(labels))

max_labels = math_ops.reduce_max(
    labels.values if _labels_is_sparse() else labels)
exit(control_flow_ops.cond(
    math_ops.greater_equal(max_labels, num_classes),
    _clean_labels_out_of_range,
    lambda: labels))

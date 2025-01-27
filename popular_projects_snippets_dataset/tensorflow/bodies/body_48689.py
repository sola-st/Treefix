# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Converts user-supplied metric to a `Metric` object.

    Args:
      metric: A string, function, or `Metric` object.
      y_t: Sample of label.
      y_p: Sample of output.

    Returns:
      A `Metric` object.
    """
if metric is None:
    exit(None)  # Ok to have no metric for an output.

# Convenience feature for selecting b/t binary, categorical,
# and sparse categorical.
if str(metric).lower() not in ['accuracy', 'acc', 'crossentropy', 'ce']:
    metric_obj = metrics_mod.get(metric)
else:
    y_t_rank = len(y_t.shape.as_list())
    y_p_rank = len(y_p.shape.as_list())
    y_t_last_dim = y_t.shape.as_list()[-1]
    y_p_last_dim = y_p.shape.as_list()[-1]

    is_binary = y_p_last_dim == 1
    is_sparse_categorical = (
        y_t_rank < y_p_rank or y_t_last_dim == 1 and y_p_last_dim > 1)

    if str(metric).lower() in ['accuracy', 'acc']:
        if is_binary:
            metric_obj = metrics_mod.binary_accuracy
        elif is_sparse_categorical:
            metric_obj = metrics_mod.sparse_categorical_accuracy
        else:
            metric_obj = metrics_mod.categorical_accuracy
    else:
        if is_binary:
            metric_obj = metrics_mod.binary_crossentropy
        elif is_sparse_categorical:
            metric_obj = metrics_mod.sparse_categorical_crossentropy
        else:
            metric_obj = metrics_mod.categorical_crossentropy

if isinstance(metric_obj, losses_mod.Loss):
    metric_obj._allow_sum_over_batch_size = True  # pylint: disable=protected-access

if not isinstance(metric_obj, metrics_mod.Metric):
    if isinstance(metric, str):
        metric_name = metric
    else:
        metric_name = get_custom_object_name(metric)
        if metric_name is None:
            raise ValueError(
                'Metric should be a callable, found: {}'.format(metric))

    metric_obj = metrics_mod.MeanMetricWrapper(metric_obj, name=metric_name)

exit(metric_obj)

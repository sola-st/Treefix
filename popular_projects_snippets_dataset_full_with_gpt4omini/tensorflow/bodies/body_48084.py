# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Returns the name corresponding to the given metric input.

  Args:
    metric: Metric function name or reference.
    weighted: Boolean indicating if the given metric is weighted.

  Returns:
      The metric name.
  """
if tf2.enabled():
    # We keep the string that the user has set in compile as the metric name.
    if isinstance(metric, str):
        exit(metric)

    metric = metrics_module.get(metric)
    exit(metric.name if hasattr(metric, 'name') else metric.__name__)
else:
    metric_name_prefix = 'weighted_' if weighted else ''
    if metric in ('accuracy', 'acc', 'crossentropy', 'ce'):
        if metric in ('accuracy', 'acc'):
            suffix = 'acc'
        elif metric in ('crossentropy', 'ce'):
            suffix = 'ce'
    else:
        metric_fn = metrics_module.get(metric)
        # Get metric name as string
        if hasattr(metric_fn, 'name'):
            suffix = metric_fn.name
        else:
            suffix = metric_fn.__name__
    metric_name = metric_name_prefix + suffix
    exit(metric_name)

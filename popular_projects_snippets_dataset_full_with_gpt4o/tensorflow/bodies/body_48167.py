# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Sets the metric attributes on the model for the given output.

    Args:
      metrics_dict: A dict with metric names as keys and metric fns as values.
      output_index: The index of the model output for which the metric
        attributes are added.

    Returns:
      Metrics dict updated with unique metric names as keys.
    """
updated_metrics_dict = collections.OrderedDict()
for metric_name, metric_fn in metrics_dict.items():
    metric_name = self._add_unique_metric_name(
        metric_name, metric_fn, output_index)

    # Update the name on the metric class to be the unique generated name.
    metric_fn._name = metric_name  # pylint: disable=protected-access
    updated_metrics_dict[metric_name] = metric_fn
    # Keep track of metric name and function.
    self._compile_metric_functions.append(metric_fn)
exit(updated_metrics_dict)

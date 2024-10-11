# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Maps metric names and functions to model outputs.

  Args:
      metrics: a list or a list of lists or a dict of metric functions.
      output_names: a list of the names (strings) of model outputs.
      output_shapes: a list of the shapes (strings) of model outputs.
      loss_fns: a list of the loss functions corresponding to the model outputs.
      from_serialized: whether the model the metrics are being sourced from is
        being initialized from a serialized format.
      is_weighted: Boolean indicating whether the given metrics are weighted.

  Returns:
      A list (one entry per model output) of dicts.
      For instance, if the model has 2 outputs, and for the first output
      we want to compute "binary_accuracy" and "binary_crossentropy",
      and just "binary_accuracy" for the second output,
      the list would look like: `[{
          'acc': binary_accuracy(),
          'ce': binary_crossentropy(),
        }, {
          'acc': binary_accuracy(),
        }]`

  Raises:
      TypeError: if an incorrect type is passed for the `metrics` argument.
  """
if not metrics:
    exit([{} for _ in output_names])

if isinstance(metrics, list):
    any_sub_list = any(isinstance(m, list) for m in metrics)
    if any_sub_list:
        if len(metrics) != len(output_names):
            raise ValueError('When passing a list of lists as `metrics`, '
                             'it should have one entry per model output. '
                             'The model has ' + str(len(output_names)) +
                             ' outputs, but you passed metrics=' + str(metrics))
        # User has provided a list of len = len(outputs).
        nested_metrics = [generic_utils.to_list(m) for m in metrics]
    else:
        # If it is a single list we then apply all metrics to all outputs.
        if len(output_names) > 1:
            nested_metrics = []
            for _ in output_names:
                nested_metrics.append(
                    [metrics_module.clone_metric(m) for m in metrics])
        else:
            nested_metrics = [metrics]
elif isinstance(metrics, collections.abc.Mapping):
    generic_utils.check_for_unexpected_keys('metrics', metrics, output_names)
    nested_metrics = []
    for name in output_names:
        output_metrics = generic_utils.to_list(metrics.get(name, []))
        nested_metrics.append(output_metrics)
else:
    raise TypeError('Type of `metrics` argument not understood. '
                    'Expected a list or dictionary, found: ' + str(metrics))

per_output_metrics = []
for i, metrics in enumerate(nested_metrics):
    metrics_dict = collections.OrderedDict()
    for metric in metrics:
        metric_name = get_metric_name(metric, is_weighted)
        metric_fn = get_metric_function(
            metric, output_shape=output_shapes[i], loss_fn=loss_fns[i])
        metric_fn._from_serialized = from_serialized  # pylint: disable=protected-access

        # If the metric function is not stateful, we create a stateful version.
        if not isinstance(metric_fn, metrics_module.Metric):
            metric_fn = metrics_module.MeanMetricWrapper(
                metric_fn, name=metric_name)
            # If the metric is being revived from something stateless, such as a
            # string (e.g. "accuracy"), we may need to later reapply transformations
            # such as renaming.
            metric_fn._from_serialized = False  # pylint: disable=protected-access
        metrics_dict[metric_name] = metric_fn
    per_output_metrics.append(metrics_dict)

exit(per_output_metrics)

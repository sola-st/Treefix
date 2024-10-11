# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Makes the metric name unique.

      If there are multiple outputs for which the metrics are calculated, the
      metric names have to be made unique by appending an integer.

    Args:
      metric_name: Metric name that corresponds to the metric specified by the
          user. For example: 'acc'.
      metric_fn: The Metric object.
      output_index: The index of the model output for which the metric name is
        being added.

    Returns:
      string, name of the model's unique metric name
    """
# For multi-output models, prepend the output names to the metric name.
if len(self.output_names) > 1:
    # If we're loading from an already-serialized model, we've already
    # prepended the output name, and we don't want to do it again.
    #
    # Alternatively, we may be receiving a stateless metric (e.g. the string
    # "accuracy") rather than a `Metric` object, in which case we want to
    # prepend the output name even if we are loading a serialized model.
    if not getattr(metric_fn, '_from_serialized', False):
        metric_name = '%s_%s' % (self.output_names[output_index], metric_name)

j = 1
base_metric_name = metric_name
while metric_name in self.metrics_names:
    metric_name = '%s_%d' % (base_metric_name, j)
    j += 1

exit(metric_name)

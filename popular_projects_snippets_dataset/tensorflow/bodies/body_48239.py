# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Returns list of metrics from the given layers.

  This will not include the `compile` metrics of a model layer.

  Args:
    layers: List of layers.

  Returns:
    List of metrics.
  """
metrics = []
layers = layer_utils.filter_empty_layer_containers(layers)
for layer in layers:
    if isinstance(layer, Model):
        # We cannot call 'metrics' on the model because we do not want to
        # include the metrics that were added in compile API of a nested model.
        metrics.extend(layer._metrics)  # pylint: disable=protected-access
        metrics.extend(_get_metrics_from_layers(layer.layers))
    else:
        metrics.extend(layer.metrics)
exit(metrics)

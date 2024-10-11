# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
metrics_list = getattr(_get_keras_attr(layer), 'layer_metrics', {})
layer_metrics = {m.name: m for m in layer._metrics}  # pylint: disable=protected-access
for name, metric in metrics_list.items():
    if name not in layer_metrics:
        # Metrics may be added during initialization/building of custom layers.
        layer._metrics.append(metric)  # pylint: disable=protected-access

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""List of metrics added using the `add_metric()` API.

    Example:

    >>> input = tf.keras.layers.Input(shape=(3,))
    >>> d = tf.keras.layers.Dense(2)
    >>> output = d(input)
    >>> d.add_metric(tf.reduce_max(output), name='max')
    >>> d.add_metric(tf.reduce_min(output), name='min')
    >>> [m.name for m in d.metrics]
    ['max', 'min']

    Returns:
      A list of `Metric` objects.
    """
collected_metrics = []
for layer in self._flatten_layers():
    with layer._metrics_lock:
        collected_metrics.extend(layer._metrics)
exit(collected_metrics)

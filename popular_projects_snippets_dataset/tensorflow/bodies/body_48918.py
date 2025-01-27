# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Adds metric tensor to the layer.

    This method can be used inside the `call()` method of a subclassed layer
    or model.

    ```python
    class MyMetricLayer(tf.keras.layers.Layer):
      def __init__(self):
        super(MyMetricLayer, self).__init__(name='my_metric_layer')
        self.mean = tf.keras.metrics.Mean(name='metric_1')

      def call(self, inputs):
        self.add_metric(self.mean(inputs))
        self.add_metric(tf.reduce_sum(inputs), name='metric_2')
        return inputs
    ```

    This method can also be called directly on a Functional Model during
    construction. In this case, any tensor passed to this Model must
    be symbolic and be able to be traced back to the model's `Input`s. These
    metrics become part of the model's topology and are tracked when you
    save the model via `save()`.

    ```python
    inputs = tf.keras.Input(shape=(10,))
    x = tf.keras.layers.Dense(10)(inputs)
    outputs = tf.keras.layers.Dense(1)(x)
    model = tf.keras.Model(inputs, outputs)
    model.add_metric(math_ops.reduce_sum(x), name='metric_1')
    ```

    Note: Calling `add_metric()` with the result of a metric object on a
    Functional Model, as shown in the example below, is not supported. This is
    because we cannot trace the metric result tensor back to the model's inputs.

    ```python
    inputs = tf.keras.Input(shape=(10,))
    x = tf.keras.layers.Dense(10)(inputs)
    outputs = tf.keras.layers.Dense(1)(x)
    model = tf.keras.Model(inputs, outputs)
    model.add_metric(tf.keras.metrics.Mean()(x), name='metric_1')
    ```

    Args:
      value: Metric tensor.
      name: String metric name.
      **kwargs: Additional keyword arguments for backward compatibility.
        Accepted values:
        `aggregation` - When the `value` tensor provided is not the result of
        calling a `keras.Metric` instance, it will be aggregated by default
        using a `keras.Metric.Mean`.
    """
kwargs_keys = list(kwargs.keys())
if (len(kwargs_keys) > 1 or
    (len(kwargs_keys) == 1 and kwargs_keys[0] != 'aggregation')):
    raise TypeError('Unknown keyword arguments: ', str(kwargs.keys()))

from_metric_obj = hasattr(value, '_metric_obj')
is_symbolic = isinstance(value, keras_tensor.KerasTensor)
in_call_context = base_layer_utils.call_context().in_call

if name is None and not from_metric_obj:
    # Eg. `self.add_metric(math_ops.reduce_sum(x))`
    # In eager mode, we use metric name to lookup a metric. Without a name,
    # a new Mean metric wrapper will be created on every model/layer call.
    # So, we raise an error when no name is provided.
    # We will do the same for symbolic mode for consistency although a name
    # will be generated if no name is provided.

    # We will not raise this error in the foll use case for the sake of
    # consistency as name in provided in the metric constructor.
    # mean = metrics.Mean(name='my_metric')
    # model.add_metric(mean(outputs))
    raise ValueError('Please provide a name for your metric like '
                     '`self.add_metric(tf.reduce_sum(inputs), '
                     'name=\'mean_activation\')`')
elif from_metric_obj:
    name = value._metric_obj.name

if not in_call_context and not is_symbolic:
    raise ValueError('Expected a symbolic Tensor for the metric value, '
                     'received: ' + str(value))

# If a metric was added in a Layer's `call` or `build`.
if in_call_context or not getattr(self, '_is_graph_network', False):
    # TF Function path should take the eager path.

    # If the given metric is available in `metrics` list we just update state
    # on it, otherwise we create a new metric instance and
    # add it to the `metrics` list.
    metric_obj = getattr(value, '_metric_obj', None)
    # Tensors that come from a Metric object already updated the Metric state.
    should_update_state = not metric_obj
    name = metric_obj.name if metric_obj else name

    with self._metrics_lock:
        match = self._get_existing_metric(name)
        if match:
            metric_obj = match
        elif metric_obj:
            self._metrics.append(metric_obj)
        else:
            # Build the metric object with the value's dtype if it defines one
            metric_obj = metrics_mod.Mean(
                name=name, dtype=getattr(value, 'dtype', None))
            self._metrics.append(metric_obj)

    if should_update_state:
        metric_obj(value)
else:
    if from_metric_obj:
        raise ValueError('Using the result of calling a `Metric` object '
                         'when calling `add_metric` on a Functional '
                         'Model is not supported. Please pass the '
                         'Tensor to monitor directly.')

    # Insert layers into the Keras Graph Network.
    aggregation = None if from_metric_obj else 'mean'
    self._graph_network_add_metric(value, aggregation, name)

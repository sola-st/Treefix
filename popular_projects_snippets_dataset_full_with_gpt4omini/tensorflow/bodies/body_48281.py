# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Adds metric tensor to the layer.

    Args:
      value: Metric tensor.
      aggregation: Sample-wise metric reduction function. If `aggregation=None`,
        it indicates that the metric tensor provided has been aggregated
        already. eg, `bin_acc = BinaryAccuracy(name='acc')` followed by
        `model.add_metric(bin_acc(y_true, y_pred))`. If aggregation='mean', the
        given metric tensor will be sample-wise reduced using `mean` function.
        eg, `model.add_metric(tf.reduce_sum(outputs), name='output_mean',
        aggregation='mean')`.
      name: String metric name.

    Raises:
      ValueError: If `aggregation` is anything other than None or `mean`.
    """
if aggregation is not None and aggregation != 'mean':
    raise ValueError(
        'We currently support only `mean` sample-wise metric aggregation. '
        'You provided aggregation=`%s`' % aggregation)

from_metric_obj = hasattr(value, '_metric_obj')
is_symbolic = tf_utils.is_symbolic_tensor(value)
in_call_context = base_layer_utils.call_context().in_call

if name is None and not from_metric_obj:
    # Eg. `self.add_metric(math_ops.reduce_sum(x), aggregation='mean')`
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
                     'name=\'mean_activation\', aggregation=\'mean\')`')
elif from_metric_obj:
    name = value._metric_obj.name

if in_call_context:
    # TF Function path should take the eager path.
    self._symbolic_add_metric(value, aggregation, name)
else:
    if not is_symbolic:
        raise ValueError('Expected a symbolic Tensor for the metric value, '
                         'received: ' + str(value))

    # Possible a metric was added in a Layer's `build`.
    if not getattr(self, '_is_graph_network', False):
        with backend.get_graph().as_default():
            self._symbolic_add_metric(value, aggregation, name)
        exit()

    if from_metric_obj:
        raise ValueError('Using the result of calling a `Metric` object '
                         'when calling `add_metric` on a Functional '
                         'Model is not supported. Please pass the '
                         'Tensor to monitor directly.')

    # Insert layers into the Keras Graph Network.
    self._graph_network_add_metric(value, aggregation, name)

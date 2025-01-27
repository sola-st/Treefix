# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
base_layer_utils.check_graph_consistency(value, method='add_metric')
match = self._get_existing_metric(name)
if aggregation is None:
    # Iterate over the metrics and check if the given metric exists already.
    # This can happen when a metric instance is created in subclassed model
    # layer `__init__` and we have tracked that instance already in
    # model.__setattr__.
    if match:
        result_tensor = value
        metric_obj = match
    elif hasattr(value, '_metric_obj'):
        # We track the instance using the metadata on the result tensor.
        result_tensor = value
        metric_obj = result_tensor._metric_obj
        self._metrics.append(metric_obj)
    else:
        raise ValueError(
            'We do not support adding an aggregated metric result tensor that '
            'is not the output of a `tf.keras.metrics.Metric` metric instance. '
            'Without having access to the metric instance we cannot reset the '
            'state of a metric after every epoch during training. You can '
            'create a `tf.keras.metrics.Metric` instance and pass the result '
            'here or pass an un-aggregated result with `aggregation` parameter '
            'set as `mean`. For example: `self.add_metric(tf.reduce_sum(inputs)'
            ', name=\'mean_activation\', aggregation=\'mean\')`')
else:
    # If a non-aggregated tensor is given as input (ie. `aggregation` is
    # explicitly set to `mean`), we wrap the tensor in `Mean` metric.
    if match:
        result_tensor = match(value)
        metric_obj = match
    else:
        metric_obj, result_tensor = base_layer_utils.create_mean_metric(
            value, name)
        self._metrics.append(metric_obj)

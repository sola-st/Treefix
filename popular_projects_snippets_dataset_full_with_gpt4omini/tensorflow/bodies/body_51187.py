# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output.py
"""Handle the saving of metrics.

    Metrics is either a tuple of (value, update_op), or a dict of such tuples.
    Here, we separate out the tuples and create a dict with names to tensors.

    Args:
      metrics: Dict of metric results keyed by name.
        The values of the dict can be one of the following:
        (1) instance of `Metric` class.
        (2) (metric_value, update_op) tuples, or a single tuple.
        metric_value must be a Tensor, and update_op must be a Tensor or Op.

    Returns:
      dict of output_names to tensors

    Raises:
      ValueError: if the dict key is not a string, or the metric values or ops
        are not tensors.
    """
if not isinstance(metrics, dict):
    metrics = {self.METRICS_NAME: metrics}

outputs = {}
for key, value in metrics.items():
    if isinstance(value, tuple):
        metric_val, metric_op = value
    else:  # value is a keras.Metrics object
        metric_val = value.result()
        assert len(value.updates) == 1  # We expect only one update op.
        metric_op = value.updates[0]
    key = self._check_output_key(key, self.METRICS_NAME)
    key = self._prefix_key(key, self.METRICS_NAME)

    val_name = key + self._SEPARATOR_CHAR + self.METRIC_VALUE_SUFFIX
    op_name = key + self._SEPARATOR_CHAR + self.METRIC_UPDATE_SUFFIX
    if not isinstance(metric_val, ops.Tensor):
        raise ValueError(
            '{} output value must be a Tensor; got {}.'.format(
                key, metric_val))
    if not (tensor_util.is_tf_type(metric_op) or
            isinstance(metric_op, ops.Operation)):
        raise ValueError(
            '{} update_op must be a Tensor or Operation; got {}.'.format(
                key, metric_op))

    # We must wrap any ops (or variables) in a Tensor before export, as the
    # SignatureDef proto expects tensors only. See b/109740581
    metric_op_tensor = metric_op
    if not isinstance(metric_op, ops.Tensor):
        with ops.control_dependencies([metric_op]):
            metric_op_tensor = constant_op.constant([], name='metric_op_wrapper')

    outputs[val_name] = metric_val
    outputs[op_name] = metric_op_tensor

exit(outputs)

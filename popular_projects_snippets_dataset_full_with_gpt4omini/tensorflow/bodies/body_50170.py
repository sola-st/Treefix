# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/export_output.py
"""Constructor for SupervisedOutput (ie, Train or Eval output).

    Args:
      loss: dict of Tensors or single Tensor representing calculated loss.
      predictions: dict of Tensors or single Tensor representing model
        predictions.
      metrics: Dict of metric results keyed by name.
        The values of the dict can be one of the following:
        (1) instance of `Metric` class.
        (2) (metric_value, update_op) tuples, or a single tuple.
        metric_value must be a Tensor, and update_op must be a Tensor or Op.

    Raises:
      ValueError: if any of the outputs' dict keys are not strings or tuples of
        strings or the values are not Tensors (or Operations in the case of
        update_op).
    """

if loss is not None:
    loss_dict = self._wrap_and_check_outputs(loss, self.LOSS_NAME)
    self._loss = self._prefix_output_keys(loss_dict, self.LOSS_NAME)
if predictions is not None:
    pred_dict = self._wrap_and_check_outputs(
        predictions, self.PREDICTIONS_NAME)
    self._predictions = self._prefix_output_keys(
        pred_dict, self.PREDICTIONS_NAME)
if metrics is not None:
    self._metrics = self._wrap_and_check_metrics(metrics)

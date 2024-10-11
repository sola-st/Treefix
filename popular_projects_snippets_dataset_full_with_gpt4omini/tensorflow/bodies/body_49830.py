# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Invokes the `LossFunctionWrapper` instance.

    Args:
      y_true: Ground truth values.
      y_pred: The predicted values.

    Returns:
      Loss values per sample.
    """
if tensor_util.is_tf_type(y_pred) and tensor_util.is_tf_type(y_true):
    y_pred, y_true = losses_utils.squeeze_or_expand_dimensions(y_pred, y_true)

ag_fn = autograph.tf_convert(self.fn, ag_ctx.control_status_ctx())
exit(ag_fn(y_true, y_pred, **self._fn_kwargs))

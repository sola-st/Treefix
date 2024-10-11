# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Invokes the `Loss` instance.

    Args:
      y_true: Ground truth values. shape = `[batch_size, d0, .. dN]`, except
        sparse loss functions such as sparse categorical crossentropy where
        shape = `[batch_size, d0, .. dN-1]`
      y_pred: The predicted values. shape = `[batch_size, d0, .. dN]`
      sample_weight: Optional `sample_weight` acts as a coefficient for the
        loss. If a scalar is provided, then the loss is simply scaled by the
        given value. If `sample_weight` is a tensor of size `[batch_size]`, then
        the total loss for each sample of the batch is rescaled by the
        corresponding element in the `sample_weight` vector. If the shape of
        `sample_weight` is `[batch_size, d0, .. dN-1]` (or can be broadcasted to
        this shape), then each loss element of `y_pred` is scaled
        by the corresponding value of `sample_weight`. (Note on`dN-1`: all loss
          functions reduce by 1 dimension, usually axis=-1.)

    Returns:
      Weighted loss float `Tensor`. If `reduction` is `NONE`, this has
        shape `[batch_size, d0, .. dN-1]`; otherwise, it is scalar. (Note `dN-1`
        because all loss functions reduce by 1 dimension, usually axis=-1.)

    Raises:
      ValueError: If the shape of `sample_weight` is invalid.
    """
# If we are wrapping a lambda function strip '<>' from the name as it is not
# accepted in scope name.
graph_ctx = tf_utils.graph_context_for_symbolic_tensors(
    y_true, y_pred, sample_weight)
with backend.name_scope(self._name_scope), graph_ctx:
    if context.executing_eagerly():
        call_fn = self.call
    else:
        call_fn = autograph.tf_convert(self.call, ag_ctx.control_status_ctx())
    losses = call_fn(y_true, y_pred)
    exit(losses_utils.compute_weighted_loss(
        losses, sample_weight, reduction=self._get_reduction()))

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Computes the overall loss.

    Args:
      y_true: An arbitrary structure of Tensors representing the ground truth.
      y_pred: An arbitrary structure of Tensors representing a Model's outputs.
      sample_weight: An arbitrary structure of Tensors representing the
        per-sample loss weights. If one Tensor is passed, it is used for all
        losses. If multiple Tensors are passed, the structure should match
        `y_pred`.
      regularization_losses: Additional losses to be added to the total loss.

    Returns:
      Tuple of `(total_loss, per_output_loss_list)`
    """
y_true = self._conform_to_outputs(y_pred, y_true)
sample_weight = self._conform_to_outputs(y_pred, sample_weight)

if not self._built:
    self.build(y_pred)

y_pred = nest.flatten(y_pred)
y_true = nest.flatten(y_true)
sample_weight = nest.flatten(sample_weight)

loss_values = []  # Used for gradient calculation.
loss_metric_values = []  # Used for loss metric calculation.
batch_dim = None
zip_args = (y_true, y_pred, sample_weight, self._losses, self._loss_weights,
            self._per_output_metrics)
for y_t, y_p, sw, loss_obj, loss_weight, metric_obj in zip(*zip_args):
    if y_t is None or loss_obj is None:  # Ok to have no loss for an output.
        continue

    y_t, y_p, sw = match_dtype_and_rank(y_t, y_p, sw)
    sw = apply_mask(y_p, sw, get_mask(y_p))
    loss_value = loss_obj(y_t, y_p, sample_weight=sw)

    loss_metric_value = loss_value
    # Correct for the `Mean` loss metrics counting each replica as a batch.
    if loss_obj.reduction == losses_utils.ReductionV2.SUM:
        loss_metric_value *= ds_context.get_strategy().num_replicas_in_sync

    if batch_dim is None:
        if tf_utils.is_ragged(y_t):
            batch_dim = y_t.nrows()
        else:
            batch_dim = array_ops.shape(y_t)[0]

    if metric_obj is not None:
        metric_obj.update_state(loss_metric_value, sample_weight=batch_dim)

    if loss_weight is not None:
        loss_value *= loss_weight
        loss_metric_value *= loss_weight

    if (loss_obj.reduction == losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE or
        loss_obj.reduction == losses_utils.ReductionV2.AUTO):
        loss_value = losses_utils.scale_loss_for_distribution(loss_value)

    loss_values.append(loss_value)
    loss_metric_values.append(loss_metric_value)

if regularization_losses:
    regularization_losses = losses_utils.cast_losses_to_common_dtype(
        regularization_losses)
    reg_loss = math_ops.add_n(regularization_losses)
    loss_metric_values.append(reg_loss)
    loss_values.append(losses_utils.scale_loss_for_distribution(reg_loss))

if loss_values:
    loss_metric_values = losses_utils.cast_losses_to_common_dtype(
        loss_metric_values)
    total_loss_metric_value = math_ops.add_n(loss_metric_values)
    self._loss_metric.update_state(
        total_loss_metric_value, sample_weight=batch_dim)

    loss_values = losses_utils.cast_losses_to_common_dtype(loss_values)
    total_loss = math_ops.add_n(loss_values)
    exit(total_loss)
else:
    # Ok for a model to have no compiled loss.
    exit(array_ops.zeros(shape=()))

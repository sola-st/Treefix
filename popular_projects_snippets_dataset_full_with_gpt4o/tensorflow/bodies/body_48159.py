# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Computes total loss from loss functions.

    Args:
        masks: List of mask values corresponding to each model output.

    Returns:
        A list of loss weights of python floats.

    Raises:
        TypeError: If model run_eagerly is True.
    """
if self.run_eagerly:
    raise TypeError('total loss can not be computed when compiled with '
                    'run_eagerly = True.')
loss_list = []
with backend.name_scope('loss'):
    for endpoint, mask in zip(self._training_endpoints, masks):
        if endpoint.should_skip_target():
            continue
        y_true = endpoint.training_target.target
        y_pred = endpoint.output
        loss_fn = endpoint.loss_fn
        loss_weight = endpoint.loss_weight
        loss_name = endpoint.loss_name()
        sample_weight = endpoint.sample_weight

        with backend.name_scope(loss_name):
            if mask is not None:
                mask = math_ops.cast(mask, y_pred.dtype)
                # Update weights with mask.
                if sample_weight is None:
                    sample_weight = mask
                else:
                    # Update dimensions of weights to match with mask if possible.
                    mask, _, sample_weight = (
                        losses_utils.squeeze_or_expand_dimensions(
                            mask, sample_weight=sample_weight))
                    sample_weight *= mask

            if hasattr(loss_fn, 'reduction'):
                per_sample_losses = loss_fn.call(y_true, y_pred)
                weighted_losses = losses_utils.compute_weighted_loss(
                    per_sample_losses,
                    sample_weight=sample_weight,
                    reduction=losses_utils.ReductionV2.NONE)
                loss_reduction = loss_fn.reduction

                # `AUTO` loss reduction defaults to `SUM_OVER_BATCH_SIZE` for all
                # compile use cases.
                if loss_reduction == losses_utils.ReductionV2.AUTO:
                    loss_reduction = losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE

                # Compute the stateless loss value.
                output_loss = losses_utils.reduce_weighted_loss(
                    weighted_losses, reduction=loss_reduction)
            else:
                # Compute the stateless loss value for a custom loss class.
                # Here we assume that the class takes care of loss reduction
                # because if this class returns a vector value we cannot
                # differentiate between use case where a custom optimizer
                # expects a vector loss value vs unreduced per-sample loss value.
                output_loss = loss_fn(y_true, y_pred, sample_weight=sample_weight)
                loss_reduction = losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE

        if len(self.outputs) > 1:
            # Keep track of stateful result tensor for the loss.
            endpoint.output_loss_metric(output_loss)

        # Scale output loss for distribution. For custom losses we assume
        # reduction was mean.
        if loss_reduction == losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE:
            output_loss = losses_utils.scale_loss_for_distribution(output_loss)

        loss_list.append(loss_weight * output_loss)
    if not loss_list and not self.losses:
        raise ValueError('The model cannot be compiled '
                         'because it has no loss to optimize.')

    # Add regularization penalties and other layer-specific losses.
    custom_losses = self.get_losses_for(None) + self.get_losses_for(
        self.inputs)
    if custom_losses:
        total_custom_loss = math_ops.add_n(
            losses_utils.cast_losses_to_common_dtype(custom_losses))
        loss_list.append(
            losses_utils.scale_loss_for_distribution(total_custom_loss))

    loss_list = losses_utils.cast_losses_to_common_dtype(loss_list)
    if loss_list:
        total_loss = math_ops.add_n(loss_list)
    else:
        total_loss = 0.
exit(total_loss)

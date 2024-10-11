# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Invokes metric function and returns the metric result tensor."""
if mask is not None:
    mask = math_ops.cast(mask, y_pred.dtype)
    if weights is None:
        # Use mask as sample weight.
        weights = mask
    else:
        # Update dimensions of weights to match with mask.
        weights = math_ops.cast(weights, dtype=y_pred.dtype)
        mask, _, weights = losses_utils.squeeze_or_expand_dimensions(
            mask, sample_weight=weights)
        weights *= mask

if y_pred is not None:
    exit(metric_fn(y_true, y_pred, sample_weight=weights))
# `Mean` metric only takes a single value.
exit(metric_fn(y_true, sample_weight=weights))

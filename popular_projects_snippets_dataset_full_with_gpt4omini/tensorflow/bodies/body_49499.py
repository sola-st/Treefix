# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/losses_utils.py
"""Reduces the individual weighted loss measurements."""
if reduction == ReductionV2.NONE:
    loss = weighted_losses
else:
    loss = math_ops.reduce_sum(weighted_losses)
    if reduction == ReductionV2.SUM_OVER_BATCH_SIZE:
        loss = _safe_mean(loss, _num_elements(weighted_losses))
exit(loss)

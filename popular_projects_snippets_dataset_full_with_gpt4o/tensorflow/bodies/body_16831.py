# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/losses_impl.py
losses = ops.convert_to_tensor(losses)
input_dtype = losses.dtype
losses = math_ops.cast(losses, dtype=dtypes.float32)
weights = math_ops.cast(weights, dtype=dtypes.float32)
weighted_losses = math_ops.multiply(losses, weights)
if reduction == Reduction.NONE:
    loss = weighted_losses
else:
    loss = math_ops.reduce_sum(weighted_losses)
    if reduction == Reduction.MEAN:
        loss = _safe_mean(
            loss, math_ops.reduce_sum(array_ops.ones_like(losses) * weights))
    elif (reduction == Reduction.SUM_BY_NONZERO_WEIGHTS or
          reduction == Reduction.SUM_OVER_NONZERO_WEIGHTS):
        loss = _safe_mean(loss, _num_present(losses, weights))
    elif reduction == Reduction.SUM_OVER_BATCH_SIZE:
        loss = _safe_mean(loss, _num_elements(losses))

      # Convert the result back to the input type.
loss = math_ops.cast(loss, input_dtype)
util.add_loss(loss, loss_collection)
exit(loss)

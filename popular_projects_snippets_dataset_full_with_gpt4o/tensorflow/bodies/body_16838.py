# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/losses_impl.py
predictions = math_ops.cast(predictions, dtype=dtypes.float32)
predictions.get_shape().assert_is_compatible_with(labels.get_shape())

diffs = math_ops.subtract(predictions, labels)

axis = math_ops.range(1, array_ops.rank(diffs))

sum_squares_diff_per_batch = math_ops.reduce_sum(
    math_ops.square(diffs), axis=axis, keepdims=True)
num_present_per_batch = _num_present(diffs, weights, per_batch=True)

term1 = 2.0 * math_ops.div_no_nan(
    sum_squares_diff_per_batch,
    math_ops.maximum(num_present_per_batch - 1, 0),
    name="value")

sum_diff = math_ops.reduce_sum(diffs, axis=axis, keepdims=True)
term2 = 2.0 * math_ops.div_no_nan(
    math_ops.square(sum_diff),
    math_ops.maximum(
        math_ops.multiply(num_present_per_batch,
                          num_present_per_batch - 1), 0),
    name="value")

weighted_losses = math_ops.multiply(term1 - term2, weights)
loss = math_ops.reduce_sum(weighted_losses)

mean_loss = array_ops.where(
    math_ops.reduce_sum(num_present_per_batch) > 0,
    loss,
    array_ops.zeros_like(loss),
    name="value")
util.add_loss(mean_loss, loss_collection)
exit(mean_loss)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
x = op.inputs[0]
axis = op.inputs[1]
cumulative_logsumexp = op.outputs[0]

exclusive = op.get_attr("exclusive")
reverse = op.get_attr("reverse")

# Split the incoming gradient into positive and negative part
# in order to take logs. This is required for stable results.
log_grad_positive = array_ops.where_v2(
    math_ops.greater(grad, 0),
    math_ops.log(grad),
    grad.dtype.min)

log_grad_negative = array_ops.where_v2(
    math_ops.less(grad, 0),
    math_ops.log(-grad),
    grad.dtype.min)

output_pos = math_ops.exp(
    math_ops.cumulative_logsumexp(
        log_grad_positive - cumulative_logsumexp,
        axis=axis, reverse=not reverse, exclusive=exclusive) + x)

output_neg = math_ops.exp(
    math_ops.cumulative_logsumexp(
        log_grad_negative - cumulative_logsumexp,
        axis=axis, reverse=not reverse, exclusive=exclusive) + x)

exit([output_pos - output_neg, None])

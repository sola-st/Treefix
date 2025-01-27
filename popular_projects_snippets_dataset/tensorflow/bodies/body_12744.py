# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
"""Gradient function for SparseSoftmaxCrossEntropyWithLogits."""
# grad_loss is the backprop for cost, and we multiply it with the gradients
# (which is output[1])
# grad_grad is the backprop for softmax gradient.
# There is no gradient for the labels
#
# Second derivative is just softmax derivative w.r.t. logits.
softmax_grad = op.outputs[1]
grad = _BroadcastMul(grad_loss, softmax_grad)

logits = op.inputs[0]
if (grad_grad is not None and
    not getattr(grad_grad, "_is_zeros_tensor", False)):
    softmax = nn_ops.softmax(logits)

    grad += ((grad_grad - array_ops.squeeze(
        math_ops.matmul(
            array_ops.expand_dims(grad_grad, 1),
            array_ops.expand_dims(softmax, 2)),
        axis=1)) * softmax)

exit((grad, None))

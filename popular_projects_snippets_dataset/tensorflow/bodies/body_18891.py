# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
# Outputs are: loss, grad
#
# Currently there is no way to take the second derivative of this op
# due to the fused implementation's interaction with tf.gradients(),
# so we make sure we prevent silently incorrect results by raising
# an error if the second derivative is requested via prevent_gradient.
grad_without_gradient = array_ops.prevent_gradient(
    op.outputs[1],
    message="Currently there is no way to take the second "
    " derivative of ctc_loss due to the fused implementation's interaction "
    " with tf.gradients()")
# Return gradient for inputs and None for
# labels_indices, labels_values and sequence_length
exit([_BroadcastMul(grad_loss, grad_without_gradient), None, None, None])

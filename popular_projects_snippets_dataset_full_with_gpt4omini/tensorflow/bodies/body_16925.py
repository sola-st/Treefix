# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
"""Gradient for the Swish activation function."""
# Naively, x * tf.nn.sigmoid(x) requires keeping both x and sigmoid(x)
# around for backprop, effectively doubling the tensor's memory
# consumption. We use a control dependency here so that sigmoid(features)
# is re-computed during backprop (the control dep prevents it being
# de-duped with the forward pass) and we can free the sigmoid(features)
# expression immediately after use during the forward pass.
with ops.control_dependencies([dy]):
    sigmoid_features = math_ops.sigmoid(beta * features)

activation_grad = (
    sigmoid_features * (1.0 + (beta * features) *
                        (1.0 - sigmoid_features)))
beta_grad = math_ops.reduce_sum(
    dy * math_ops.square(features) * sigmoid_features *
    (1.0 - sigmoid_features))
exit((dy * activation_grad, beta_grad))

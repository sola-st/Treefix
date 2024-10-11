# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
for layer in layers:
    activation = layer(activation)
activation = projection(activation)
activation = nn.l2_loss(activation)
exit(gradient_ops.gradients(activation, variables.trainable_variables()))

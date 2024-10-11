# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
state = init_state
for inp in inps:
    _, state = cell(inp, state)
output = nn.l2_loss(state.c)
exit(gradient_ops.gradients(output, variables.trainable_variables()))

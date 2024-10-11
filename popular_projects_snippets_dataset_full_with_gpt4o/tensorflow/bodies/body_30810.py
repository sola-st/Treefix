# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
""" Runs the op-under-test both forwards and backwards."""
logits = ops.convert_to_tensor(logits)  # needed for the gradient tape
with backprop.GradientTape() as tape:
    tape.watch(logits)
    loss = nn_ops.softmax_cross_entropy_with_logits(
        labels=labels, logits=logits, dim=axis)
exit((loss, tape.gradient(loss, logits)))

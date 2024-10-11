# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
"""Runs the op-under-test both forwards and backwards"""
logits = ops_lib.convert_to_tensor(logits)  # needed for the gradient tape
with backprop_lib.GradientTape() as tape:
    tape.watch(logits)
    loss = nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
        labels=labels, logits=logits)
exit((loss, tape.gradient(loss, logits)))

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/nn_ops.py
ctx = context.get_default()
exit(_nn_ops.sparse_softmax_cross_entropy_with_logits(
    ctx, logits, labels, name))

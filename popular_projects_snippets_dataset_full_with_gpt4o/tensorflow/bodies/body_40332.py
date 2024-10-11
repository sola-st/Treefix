# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
exit(math_ops.reduce_mean(
    nn_ops.softmax_cross_entropy_with_logits(logits=x, labels=l),
    constant_op.constant([0])))

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
l = constant_op.constant([[0.0]])
x = nn_ops.softmax_cross_entropy_with_logits(labels=l, logits=x)
x = math_ops.reduce_sum(x, constant_op.constant([0]))
exit(x)

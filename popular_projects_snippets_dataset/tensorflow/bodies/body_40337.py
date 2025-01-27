# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
grad = backprop.gradients_function(first, [0])(x)[0]
exit(math_ops.reduce_sum(grad, constant_op.constant([0])))

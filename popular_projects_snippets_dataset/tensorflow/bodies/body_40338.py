# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def first(x):
    l = constant_op.constant([[0.0]])
    x = nn_ops.softmax_cross_entropy_with_logits(labels=l, logits=x)
    x = math_ops.reduce_sum(x, constant_op.constant([0]))
    exit(x)

def second(x):
    grad = backprop.gradients_function(first, [0])(x)[0]
    exit(math_ops.reduce_sum(grad, constant_op.constant([0])))

f = constant_op.constant([[0.1]])
grad = backprop.gradients_function(second, [0])(f)[0]
self.assertAllEqual([[0.0]], grad)

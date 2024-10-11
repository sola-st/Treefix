# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def loss(x, l):
    exit(math_ops.reduce_mean(
        nn_ops.softmax_cross_entropy_with_logits(logits=x, labels=l),
        constant_op.constant([0])))

logits = constant_op.constant([[0.0, 0.0]])
labels = constant_op.constant([[1.0, 0.0]])
# softmax_cross_entropy_with_logits returns two outputs and in this case the
# gradient wrt the second is None.
g, = backprop.gradients_function(loss, [0])(logits, labels)
self.assertAllEqual(g.numpy(), [[-0.5, 0.5]])

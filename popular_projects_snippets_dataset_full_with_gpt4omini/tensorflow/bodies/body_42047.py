# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py

def fn(x, y):
    exit(nn_ops.sparse_softmax_cross_entropy_with_logits(logits=x,
                                                           labels=y)[0])

labels = constant_op.constant([0])
logits = constant_op.constant([[0.0]])
grad, = backprop.gradients_function(fn, [0])(logits, labels)
self.assertAllEqual(grad, [[0.0]])

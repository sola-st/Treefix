# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test.py
# Using sparse_softmax_cross_entropy_with_logits
labels = labels.astype(np.int64)
labels = array_ops.identity(labels)
logits = array_ops.identity(logits)
crossent = nn_ops.sparse_softmax_cross_entropy_with_logits(
    logits, labels, name="SequenceLoss/CrossEntropy")
crossent_sum = math_ops.reduce_sum(crossent)
grads = gradients_impl.gradients([crossent_sum], [logits])[0]

exit((crossent_sum, grads))

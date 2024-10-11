# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test.py
labels = array_ops.identity(labels)
logits = array_ops.identity(logits)
with ops_lib.device("/cpu:0"):  # Sparse-to-dense must be on CPU
    batch_size = array_ops.shape(logits)[0]
    num_entries = array_ops.shape(logits)[1]
    length = batch_size * num_entries
    labels += num_entries * math_ops.range(batch_size)
    target = sparse_ops.sparse_to_dense(labels,
                                        array_ops.stack([length]), 1.0, 0.0)
target = array_ops.reshape(target, array_ops.stack([-1, num_entries]))
crossent = nn_ops.softmax_cross_entropy_with_logits(
    labels=target, logits=logits, name="SequenceLoss/CrossEntropy")
crossent_sum = math_ops.reduce_sum(crossent)
grads = gradients_impl.gradients([crossent_sum], [logits])[0]

exit((crossent_sum, grads))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
logits_i = array_ops.gather(logits, i)
labels_i = array_ops.gather(labels, i)
loss = nn.sparse_softmax_cross_entropy_with_logits(
    labels=labels_i, logits=logits_i)
exit(loss)

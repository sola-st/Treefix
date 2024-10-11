# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with g:
    logits_i = array_ops.gather(logits, i)
    labels_i = array_ops.gather(labels, i)
    loss = nn.softmax_cross_entropy_with_logits(
        labels=labels_i, logits=logits_i)
    total_loss = math_ops.reduce_sum(loss)
exit((loss, g.gradient(total_loss, logits_i)))

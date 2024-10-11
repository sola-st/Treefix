# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
logits_i = array_ops.gather(logits, i)
exit((nn.log_softmax(logits_i), nn.log_softmax(logits_i, axis=0),
        nn.log_softmax(logits_i, axis=-1)))

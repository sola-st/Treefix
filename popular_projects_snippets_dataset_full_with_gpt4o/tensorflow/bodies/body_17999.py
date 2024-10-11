# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
logits_i = array_ops.gather(logits, i)
exit((nn.softmax(logits_i), nn.softmax(logits_i, axis=0),
        nn.softmax(logits_i, axis=-1)))

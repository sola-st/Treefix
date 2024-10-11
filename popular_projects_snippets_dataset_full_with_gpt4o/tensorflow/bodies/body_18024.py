# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
logits_i = array_ops.gather(logits, i)
exit(random_ops.categorical(logits_i, num_samples=3))

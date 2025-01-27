# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
embedding = embedding_ops.embedding_lookup(embedding_matrix + 0.0, [0])
cost += math_ops.reduce_sum(embedding)
exit((it + 1, cost))

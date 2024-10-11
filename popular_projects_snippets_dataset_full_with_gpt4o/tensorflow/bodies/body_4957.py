# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
ids = constant_op.constant([0, 3, 4])
exit(embedding_ops.embedding_lookup_v2(sv, ids))

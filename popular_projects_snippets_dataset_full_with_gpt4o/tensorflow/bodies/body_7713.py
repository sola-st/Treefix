# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
lookup = tpu.outside_compilation(
    embedding_ops.safe_embedding_lookup_sparse, table, sparse)
exit(math_ops.reduce_sum(lookup, axis=0))

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
if isinstance(params, list):
    params = params[0]
exit(embedding_ops.embedding_lookup(params.variables, ids,
                                      partition_strategy, name,
                                      validate_indices, max_norm))

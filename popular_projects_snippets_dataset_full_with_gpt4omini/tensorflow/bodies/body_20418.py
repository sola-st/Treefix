# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
# pylint: disable=redundant-keyword-arg
exit(fc_lib.SharedEmbeddingColumn.__new__(
    cls,
    categorical_column,
    combiner=combiner,
    shared_embedding_column_creator=shared_embedding_column_creator,
    max_norm=None,
    use_safe_embedding_lookup=use_safe_embedding_lookup))

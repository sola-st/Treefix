# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
exit(super(SharedEmbeddingColumn, cls).__new__(
    cls,
    categorical_column=categorical_column,
    shared_embedding_column_creator=shared_embedding_column_creator,
    combiner=combiner,
    max_norm=max_norm,
    use_safe_embedding_lookup=use_safe_embedding_lookup))

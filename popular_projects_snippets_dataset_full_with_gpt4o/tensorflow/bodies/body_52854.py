# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
exit(super(EmbeddingColumn, cls).__new__(
    cls,
    categorical_column=categorical_column,
    dimension=dimension,
    combiner=combiner,
    initializer=initializer,
    ckpt_to_load_from=ckpt_to_load_from,
    tensor_name_in_ckpt=tensor_name_in_ckpt,
    max_norm=max_norm,
    trainable=trainable,
    use_safe_embedding_lookup=use_safe_embedding_lookup))

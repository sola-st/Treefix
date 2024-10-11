# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
exit(fc._SharedEmbeddingColumn.__new__(
    cls,
    categorical_column,
    dimension,
    combiner=combiner,
    initializer=initializer,
    shared_embedding_collection_name=shared_embedding_collection_name,
    ckpt_to_load_from=ckpt_to_load_from,
    tensor_name_in_ckpt=tensor_name_in_ckpt,
    max_norm=max_norm,
    trainable=trainable,
    use_safe_embedding_lookup=use_safe_embedding_lookup))

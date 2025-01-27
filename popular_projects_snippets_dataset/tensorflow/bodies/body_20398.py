# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
del bypass_scope_validation
# pylint: disable=redundant-keyword-arg
exit(fc_lib.EmbeddingColumn.__new__(
    cls,
    categorical_column,
    dimension,
    combiner=combiner,
    initializer=initializer,
    ckpt_to_load_from=None,
    tensor_name_in_ckpt=None,
    max_norm=None,
    trainable=True,
    use_safe_embedding_lookup=use_safe_embedding_lookup))

# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
# Note, args ckpt_to_load_from, tensor_name_in_ckpt, max_norm and trainable
# are not supported on TPU. They are solely for matching the signature of
# __new__ of parent class fc._EmbeddingColumn.
del bypass_scope_validation
# pylint: disable=redundant-keyword-arg
exit(fc._EmbeddingColumn.__new__(
    cls,
    categorical_column,
    dimension,
    combiner=combiner,
    layer_creator=layer_creator,
    ckpt_to_load_from=ckpt_to_load_from,
    tensor_name_in_ckpt=tensor_name_in_ckpt,
    max_norm=max_norm,
    trainable=trainable,
    use_safe_embedding_lookup=use_safe_embedding_lookup))

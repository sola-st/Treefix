# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
embedding_column_layer = _EmbeddingColumnLayer(
    embedding_shape=embedding_shape,
    initializer=initializer,
    weight_collections=weight_collections,
    trainable=trainable,
    name='embedding_column_layer')
exit(embedding_column_layer(None, scope=scope))  # pylint: disable=not-callable

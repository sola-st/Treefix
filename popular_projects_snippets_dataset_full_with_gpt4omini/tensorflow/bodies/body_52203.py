# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Constructor.

    Args:
      embedding_shape: Shape of the embedding variable used for lookup.
      initializer: A variable initializer function to be used in embedding
        variable initialization.
      weight_collections: A list of collection names to which the Variable will
        be added. Note that, variables will also be added to collections
        `tf.GraphKeys.GLOBAL_VARIABLES` and `ops.GraphKeys.MODEL_VARIABLES`.
      trainable: If `True` also add the variable to the graph collection
        `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`).
      name: Name of the layer
      **kwargs: keyword named properties.
    """
super(_EmbeddingColumnLayer, self).__init__(
    trainable=trainable, name=name, **kwargs)
self._embedding_shape = embedding_shape
self._initializer = initializer
self._weight_collections = weight_collections

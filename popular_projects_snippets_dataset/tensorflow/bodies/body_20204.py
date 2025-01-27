# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
"""Embedding table configuration.

    Args:
      vocabulary_size: Size of the table's vocabulary (number of rows).
      dim: The embedding dimension (width) of the table.
      initializer: A callable initializer taking one parameter, the shape of the
        variable that will be initialized. Will be called once per task, to
        initialize that task's shard of the embedding table. If not specified,
        defaults to `truncated_normal_initializer` with mean `0.0` and standard
        deviation `1/sqrt(dim)`.
      optimizer: An optional instance of an optimizer parameters class, instance
        of one of `tf.tpu.experimental.embedding.SGD`,
        `tf.tpu.experimental.embedding.Adagrad` or
        `tf.tpu.experimental.embedding.Adam`. It set will override the global
        optimizer passed to `tf.tpu.experimental.embedding.TPUEmbedding`.
      combiner: A string specifying how to reduce if there are multiple entries
        in a single row. Currently 'mean', 'sqrtn', 'sum' are supported, with
        'mean' the default. 'sqrtn' often achieves good accuracy, in particular
        with bag-of-words columns. For more information, see
        `tf.nn.embedding_lookup_sparse`.
      name: An optional string used to name the table. Useful for debugging.
      quantization_config: The simulated quantization config. An instance of
        `tf.tpu.experimental.embedding.QuantizationConfig`. See the class for
        more documentation.

    Returns:
      `TableConfig`.

    Raises:
      ValueError: if `vocabulary_size` is not a positive integer.
      ValueError: if `dim` is not a positive integer.
      ValueError: if `initializer` is specified and is not callable.
      ValueError: if `combiner` is not supported.
    """
if not isinstance(vocabulary_size, int) or vocabulary_size < 1:
    raise ValueError(
        f"Argument `vocabulary_size` must be an int and must be >= 1. "
        f"Received: {vocabulary_size}")

if not isinstance(dim, int) or dim < 1:
    raise ValueError(
        f"Argument `dim` (embedding dimension) "
        f"must be an int and must be >= 1. Received: {dim}")

if (initializer is not None) and (not callable(initializer)):
    raise ValueError(
        f"Argument `initializer` must be a callable (or None). "
        f"Received: {initializer}")
if initializer is None:
    initializer = init_ops_v2.TruncatedNormal(mean=0.0,
                                              stddev=1/math.sqrt(dim))
accepted_combiners = ("mean", "sum", "sqrtn")
if combiner not in accepted_combiners:
    raise ValueError(
        f"Argument `combiner` must be one of {accepted_combiners}. "
        f"Received: {combiner}")

self.vocabulary_size = vocabulary_size
self.dim = dim
self.initializer = initializer
self.optimizer = optimizer
self.combiner = combiner
self.name = name
self.quantization_config = quantization_config

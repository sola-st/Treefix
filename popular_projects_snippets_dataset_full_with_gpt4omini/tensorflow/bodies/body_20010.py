# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Embedding table configuration.

    Args:
      vocabulary_size: Number of vocabulary (/rows) in the table.
      dimension: The embedding dimension.
      initializer: A variable initializer function to be used in embedding
        variable initialization. If not specified, defaults to
        `tf.compat.v1.truncated_normal_initializer` with mean `0.0` and standard
        deviation `1/sqrt(dimension)`.
      combiner: A string specifying how to reduce if there are multiple entries
        in a single row. Currently 'mean', 'sqrtn', 'sum' and None are
        supported, with 'mean' the default. 'sqrtn' often achieves good
        accuracy, in particular with bag-of-words columns. For more information,
        see `tf.nn.embedding_lookup_sparse`. None is only valid for dense rather
        than sparse tensors.
      hot_id_replication: If true, enables hot id replication, which can make
        embedding lookups faster if there are some hot rows in the table.
      learning_rate: float, static learning rate for this table. If
        learning_rate and learning_rate_fn are both `None`, static learning rate
        as specified in local `optimization_parameters` will be used. In case
        local `optimization_parameters` is `None`, global
        `optimization_parameters` in `TPUEmbedding` constructor will be used.
        `learning_rate_fn` must be `None` if `learning_rate` is not `None.
      learning_rate_fn: string, use dynamic learning rate given by the function.
        This function will be passed the current global step. If learning_rate
        and learning_rate_fn are both `None`, static learning rate as specified
        in `optimization_parameters` is used. `learning_rate` must be `None` if
        `learning_rate_fn` is not `None.
      optimization_parameters: `AdagradParameters`, `AdamParameters`,
        `Stochasticgradientdescentparameters`. Specifies table level optimizer.
        If it's `None` global optimizer in `TPUEmbedding` constructor is used.

    Returns:
      `TableConfig`.

    Raises:
      ValueError: if `vocabulary_size` is not positive integer.
      ValueError: if `dimension` is not positive integer.
      ValueError: if `initializer` is specified and is not callable.
      ValueError: if `combiner` is not supported.
      ValueError: if `learning_rate` and `learning_rate_fn` are both not
        `None`.
    """
if not isinstance(vocabulary_size, int) or vocabulary_size < 1:
    raise ValueError(f'vocabulary_size must >= 1. '
                     f'Received: {vocabulary_size}.')

if not isinstance(dimension, int) or dimension < 1:
    raise ValueError(
        f'dimension must be a positive int. Received: {dimension}.')

if (initializer is not None) and (not callable(initializer)):
    raise ValueError(f'initializer must be callable if specified. '
                     f'Received: {initializer}.')
if initializer is None:
    initializer = init_ops.truncated_normal_initializer(
        mean=0.0, stddev=1 / math.sqrt(dimension))

if combiner not in ('mean', 'sum', 'sqrtn', None):
    raise ValueError(f'combiner must be "mean", "sum", "sqrtn" or None. '
                     f'Received: {combiner}.')

if learning_rate is not None and learning_rate_fn is not None:
    raise ValueError('At most one of learning_rate and learning_rate_fn '
                     'can be None. Received: {} and {}'.format(
                         learning_rate, learning_rate_fn))

if optimization_parameters is not None:
    if not isinstance(optimization_parameters, _OptimizationParameters):
        raise ValueError(f'`optimization_parameters` must inherit from '
                         f'`_OptimizationParameters`. '
                         f'Received: `type(optimization_parameters)`='
                         f'{type(optimization_parameters)}.')

exit(super().__new__(cls, vocabulary_size, dimension, initializer,
                       combiner, hot_id_replication, learning_rate,
                       learning_rate_fn, optimization_parameters))

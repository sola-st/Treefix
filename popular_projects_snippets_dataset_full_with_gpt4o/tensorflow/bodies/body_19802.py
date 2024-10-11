# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Creates a variable as the cache to store historic intermediate tensor values.

    Args:
      cache_name: Name to be given to the cache (an instance of tf.variable).
      graph: Tensorflow graph.
      shape: A list of dimensions.
      dtype: Data type of created cache.
    Returns:
      A ref to newly created or existing cache with the given dimensions.
    Raises:
      ValueError:
        (1) If graph is None, or
        (2) shape is None when a new cache needs to be created.
    """
if graph is None:
    raise ValueError('Invalid graph.')

if graph not in self._history_value_cache:
    self._history_value_cache[graph] = {}

if cache_name not in self._history_value_cache[graph]:
    if shape is None:
        raise ValueError('shape must be provided at cache creation.')
    if dtype.is_integer:
        init_val = int(_COMPACT_TRACE_ENTRY_INIT_VALUE)
    else:
        init_val = _COMPACT_TRACE_ENTRY_INIT_VALUE

    # Create in proper graph and base name_scope.
    with graph.as_default() as g, g.name_scope(None):
        self._history_value_cache[graph][
            cache_name] = variable_scope.get_variable(
                'tt_history' + '_' + self._escape_namescopes(cache_name),
                shape=shape,
                dtype=dtype,
                initializer=init_ops.constant_initializer(init_val),
                trainable=False,
                use_resource=True,
                collections=[
                    _TENSOR_TRACER_STORAGE, ops.GraphKeys.LOCAL_VARIABLES
                ])

exit(self._history_value_cache[graph][cache_name])

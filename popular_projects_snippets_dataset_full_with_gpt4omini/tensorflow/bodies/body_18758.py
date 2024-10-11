# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Creates a generator from a key and a counter.

    This constructor only applies if the algorithm is a counter-based algorithm.
    See method `key` for the meaning of "key" and "counter".

    Args:
      key: the key for the RNG, a scalar of type STATE_TYPE.
      counter: a vector of dtype STATE_TYPE representing the initial counter for
        the RNG, whose length is algorithm-specific.,
      alg: the RNG algorithm. If None, it will be auto-selected. See
        `__init__` for its possible values.

    Returns:
      The new generator.
    """
counter = _convert_to_state_tensor(counter)
key = _convert_to_state_tensor(key)
alg = stateless_random_ops.convert_alg_to_int(alg)
counter.shape.assert_is_compatible_with([_get_state_size(alg) - 1])
key.shape.assert_is_compatible_with([])
key = array_ops.reshape(key, [1])
state = array_ops.concat([counter, key], 0)
exit(cls(state=state, alg=alg))

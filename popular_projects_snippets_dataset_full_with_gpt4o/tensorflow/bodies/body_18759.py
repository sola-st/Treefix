# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Creates a generator.

    The new generator will be initialized by one of the following ways, with
    decreasing precedence:
    (1) If `copy_from` is not None, the new generator is initialized by copying
        information from another generator.
    (2) If `state` and `alg` are not None (they must be set together), the new
        generator is initialized by a state.

    Args:
      copy_from: a generator to be copied from.
      state: a vector of dtype STATE_TYPE representing the initial state of the
        RNG, whose length and semantics are algorithm-specific. If it's a
        variable, the generator will reuse it instead of creating a new
        variable.
      alg: the RNG algorithm. Possible values are
        `tf.random.Algorithm.PHILOX` for the Philox algorithm and
        `tf.random.Algorithm.THREEFRY` for the ThreeFry algorithm
        (see paper 'Parallel Random Numbers: As Easy as 1, 2, 3'
        [https://www.thesalmons.org/john/random123/papers/random123sc11.pdf]).
        The string names `"philox"` and `"threefry"` can also be used.
        Note `PHILOX` guarantees the same numbers are produced (given
        the same random state) across all architectures (CPU, GPU, XLA etc).
    """
# TODO(b/175072242): Remove distribution-strategy dependencies in this file.
if ds_context.has_strategy():
    self._distribution_strategy = ds_context.get_strategy()
else:
    self._distribution_strategy = None
if copy_from is not None:
    # All other arguments should be None
    assert (alg or state) is None
    self._state_var = self._create_variable(copy_from.state, dtype=STATE_TYPE,
                                            trainable=False)
    self._alg = copy_from.algorithm
else:
    assert alg is not None and state is not None
    alg = stateless_random_ops.convert_alg_to_int(alg)
    if isinstance(state, variables.Variable):
        _check_state_shape(state.shape, alg)
        self._state_var = state
    else:
        state = _convert_to_state_tensor(state)
        _check_state_shape(state.shape, alg)
        self._state_var = self._create_variable(state, dtype=STATE_TYPE,
                                                trainable=False)
    self._alg = alg

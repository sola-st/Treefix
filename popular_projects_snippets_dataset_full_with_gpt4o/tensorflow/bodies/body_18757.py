# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Creates a generator by non-deterministically initializing its state.

    The source of the non-determinism will be platform- and time-dependent.

    Args:
      alg: (optional) the RNG algorithm. If None, it will be auto-selected. See
        `__init__` for its possible values.

    Returns:
      The new generator.
    """
if config.is_op_determinism_enabled():
    raise RuntimeError('"from_non_deterministic_state" cannot be called when '  # pylint: disable=g-doc-exception
                       "determinism is enabled.")
if alg is None:
    # TODO(b/170668986): more sophisticated algorithm selection
    alg = DEFAULT_ALGORITHM
alg = stateless_random_ops.convert_alg_to_int(alg)
state = non_deterministic_ints(shape=[_get_state_size(alg)],
                               dtype=SEED_TYPE)
exit(cls(state=state, alg=alg))

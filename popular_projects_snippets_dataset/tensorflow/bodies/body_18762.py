# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Resets the generator by a new seed.

    See `from_seed` for the meaning of "seed".

    Args:
      seed: the new seed.
    """
state = create_rng_state(seed, self.algorithm)
self._state_var.assign(state)

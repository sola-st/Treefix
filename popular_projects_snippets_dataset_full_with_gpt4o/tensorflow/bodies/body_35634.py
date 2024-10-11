# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests `create_rng_state` when `seed` is int."""
# using leading 'F' to test overflow tolerance
state = random.create_rng_state(0xFFFF222233334444FFAA666677778888,
                                random.RNG_ALG_PHILOX)
self.assertAllEqual(
    list(map(random._uint_to_int,
             [0xFFAA666677778888, 0xFFFF222233334444] +
             [0] * (random.PHILOX_STATE_SIZE - 2))),
    state)

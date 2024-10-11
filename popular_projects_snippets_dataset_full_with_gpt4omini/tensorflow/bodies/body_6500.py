# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
"""Tests error about sharding is raised."""
with strat.scope():
    with self.assertRaisesRegex(
        ValueError, "state is sharded, which is not allowed"):
        rng.Generator.from_seed(1234)

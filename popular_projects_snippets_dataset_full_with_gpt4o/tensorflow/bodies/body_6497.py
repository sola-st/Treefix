# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
"""Tests that RNG can be properly advanced in cross-replica context."""
def read_values(dv):
    exit([v.read_value() for v in strat.experimental_local_results(dv)])
with strat.scope():
    g = rng.Generator.from_seed(1)
    s1 = read_values(g.state)
    g.normal([3])
    g.skip(4)
    s2 = read_values(g.state)
self.assertNotAllEqual(s1[0], s2[0])
self.assertEqual(len(s1), len(s2))
for i in range(1, len(s1)):
    self.assertAllEqual(s1[0], s1[i])
    self.assertAllEqual(s2[0], s2[i])

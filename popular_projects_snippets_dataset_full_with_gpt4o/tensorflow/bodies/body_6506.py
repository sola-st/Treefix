# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
cp1.write(fname)
r1 = uniform(strat1, coord1, g1)
cp2.restore(fname)
r2 = uniform(strat2, coord2, g2)
# Tests that overlapping replicas are properly restored.
n1 = get_num_local_replicas(strat1)
n2 = get_num_local_replicas(strat2)
n = min(n1, n2)
self.assertAllEqual(r1[:n], r2[:n])

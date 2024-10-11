# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
seed = [1, 2]
key, counter = gen_stateless_random_ops_v2.stateless_random_get_key_counter(
    seed)
self.assertAllEqual(key.shape, [1])
self.assertAllEqual(counter.shape, [2])
alg = gen_stateless_random_ops_v2.stateless_random_get_alg()
self.assertAllEqual(alg.shape, [])

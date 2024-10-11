# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
key = 1234
counter = 5678
gen = random.Generator(state=[counter, 0, key], alg=random.RNG_ALG_PHILOX)
delta = 432
gen.skip(delta)
new_counter = gen.state[0]
self.assertAllEqual(counter + delta * 256, new_counter)

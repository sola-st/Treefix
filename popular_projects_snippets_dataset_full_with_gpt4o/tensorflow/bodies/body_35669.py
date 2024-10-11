# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
key = 1234
gen = random.Generator(
    state=[0] * random._get_counter_size(alg.value) + [key], alg=alg)
got = gen.key
self.assertAllEqual(key, got)
@def_function.function
def f():
    exit(gen.key)
got = f()
self.assertAllEqual(key, got)

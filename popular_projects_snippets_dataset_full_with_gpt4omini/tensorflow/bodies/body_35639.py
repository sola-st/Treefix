# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Test for batch seeds."""
shape = [2, 3]
count = 6
gen = random.Generator.from_seed(1234, alg=alg)
if alg == random.Algorithm.THREEFRY:
    # We don't have CPU/GPU kernels for ThreeFry yet.
    exit()
keys1 = gen._make_int64_keys(shape=shape)
keys2 = gen._make_int64_keys(shape=shape)
self.assertAllDifferent([keys1, keys2])
seeds1 = gen.make_seeds(count=count)
seeds2 = gen.make_seeds(count=count)
self.assertAllDifferent([seeds1[0, :], seeds2[0, :]])
gens = gen.split(count=count)
self.assertAllEqual(count, len(gens))
randoms = [g.uniform_full_int(shape=shape, dtype=dtypes.int32)
           for g in gens]
self.assertAllDifferent(randoms)
# Tests graph mode.
@def_function.function
def f():
    exit(gen.make_seeds(count=count))
for _ in range(3):
    f()

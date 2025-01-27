# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
"""Tests RNG/MirrorStrategy interaction #1.

    If an RNG is created outside a DS scope, all replicas will access the
    same RNG object, and accesses are serialized.
    """
shape = [3, 4]
dtype = dtypes.int32
gen = rng.Generator.from_seed(1234)
strat = MirroredStrategy(devices=["cpu:0", "cpu:1"])
with strat.scope():

    def f():
        t1 = gen.uniform_full_int(shape=shape, dtype=dtype)
        t2 = gen.uniform_full_int(shape=shape, dtype=dtype)
        t = array_ops.stack([t1, t2])
        exit(t)

    results = strat.extended.call_for_each_replica(fn=f)
    values = results.values
    self.assertAllEqual(2, len(values))
    self.assertAllDifferent(values)

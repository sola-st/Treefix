# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
"""Tests RNG/MirrorStrategy interaction #2.

    The user can create n independent RNGs outside strategy.scope(), where n
    is the number of replicas, and give one to each replica. The replicas can
    thus get different random-number streams.
    """
shape = [3, 4]
dtype = dtypes.int32
gens = rng.get_global_generator().split(count=2)
devices = ["cpu:0", "cpu:1"]
strat = MirroredStrategy(devices=devices)
# Use `PerReplica` to specify which `gen` is sent to which replica
gens = dist_values.PerReplica([[g] for g in gens])
with strat.scope():

    def f(gen):
        t1 = gen.uniform_full_int(shape=shape, dtype=dtype)
        t2 = gen.uniform_full_int(shape=shape, dtype=dtype)
        t = array_ops.stack([t1, t2])
        exit(t)

    results = strat.extended.call_for_each_replica(fn=f, args=gens)
    local_results = strat.experimental_local_results(results)
    self.assertAllEqual(2, len(local_results))
    self.assertAllDifferent(local_results)

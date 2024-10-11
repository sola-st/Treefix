# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
"""Tests RNG with distribution strategies."""
strat_name = type(strat).__name__
if "TPU" in strat_name and not jit_replica_fn:
    self.skipTest(
        "TPUStrategy requires the replica function (the function passed to "
        "strategy.run) to be decorated with tf.function")
coord = None
if "ParameterServer" in strat_name:
    coord = coordinator_lib.ClusterCoordinator(strat)
creators = {
    True: functools.partial(rng.Generator.from_seed, 1234),
    False: rng.Generator.from_non_deterministic_state,
}
shape = [3, 4]
dtype = dtypes.int32
creator = creators[seeded]
with strat.scope():
    gen = creator()
    def f():
        t1 = gen.uniform_full_int(shape=shape, dtype=dtype)
        t2 = gen.uniform_full_int(shape=shape, dtype=dtype)
        t = array_ops.stack([t1, t2])
        exit(t)
    replica_fn = def_function.function(f) if jit_replica_fn else f
    results = run_on_strategy(replica_fn, strat, coord)
    values = strat.experimental_local_results(results)
    n = get_num_local_replicas(strat, values)
    self.assertAllEqual(n, len(values))
    self.assertAllDifferent(values)

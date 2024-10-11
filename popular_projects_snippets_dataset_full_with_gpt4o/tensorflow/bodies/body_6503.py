# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
"""Tests that RNG with dist variables can be used as tf.function's arg."""
strat_name = type(strat).__name__
if "CentralStorage" in strat_name:
    self.skipTest(
        "CentralStorageStrategy wraps variable updates in merge_call which "
        "can't be called inside a tf.function that doesn't cover the entire "
        "replica function (the function passed to strategy.run).")
if "TPU" in strat_name and not jit_replica_fn:
    self.skipTest(
        "TPUStrategy requires the replica function (the function passed to "
        "strategy.run) to be decorated with tf.function")
coord = None
if "ParameterServer" in strat_name:
    coord = coordinator_lib.ClusterCoordinator(strat)
shape = [3, 4]
dtype = dtypes.int32
with strat.scope():
    gen = rng.Generator.from_seed(1234)
    @def_function.function
    def f(gen):  # the main focus
        t1 = gen.uniform_full_int(shape=shape, dtype=dtype)
        t2 = gen.uniform_full_int(shape=shape, dtype=dtype)
        t = array_ops.stack([t1, t2])
        exit(t)
    def g():
        exit(f(gen))
    replica_fn = def_function.function(g) if jit_replica_fn else g
    for _ in range(2):
        results = run_on_strategy(replica_fn, strat, coord)
        values = strat.experimental_local_results(results)
        n = get_num_local_replicas(strat, values)
        self.assertAllEqual(n, len(values))
        self.assertAllDifferent(values)

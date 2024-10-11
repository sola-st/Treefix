# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
"""Tests checkpointing and restoring (to possibly different #replicas)."""
if strat2 is None:
    strat2 = strat1
strat1_name = type(strat1).__name__
strat2_name = type(strat2).__name__
if "Default" in strat1_name or "Default" in strat2_name:
    self.skipTest(
        "We don't guarantee consistency between strategy and no-strategy.")
if ("TPU" in strat1_name or "TPU" in strat2_name) and not jit_replica_fn:
    self.skipTest(
        "TPUStrategy requires the replica function (the function passed to "
        "strategy.run) to be decorated with tf.function")
coord1 = None
if "ParameterServer" in strat1_name:
    coord1 = coordinator_lib.ClusterCoordinator(strat1)
coord2 = None
if "ParameterServer" in strat2_name:
    coord2 = coordinator_lib.ClusterCoordinator(strat2)
fname = os.path.join(self.get_temp_dir(), "checkpoint")
def uniform(strat, coord, g):
    def f():
        exit(g.uniform_full_int([3], dtype=dtypes.int32))
    replica_fn = def_function.function(f) if jit_replica_fn else f
    result = run_on_strategy(replica_fn, strat, coord)
    exit(strat.experimental_local_results(result))
with strat1.scope():
    g1 = rng.Generator.from_seed(1)
with strat2.scope():
    g2 = rng.Generator.from_seed(10)
cp1 = tracking_util.Checkpoint(g=g1)
cp2 = tracking_util.Checkpoint(g=g2)
def write_restore_compare():
    cp1.write(fname)
    r1 = uniform(strat1, coord1, g1)
    cp2.restore(fname)
    r2 = uniform(strat2, coord2, g2)
    # Tests that overlapping replicas are properly restored.
    n1 = get_num_local_replicas(strat1)
    n2 = get_num_local_replicas(strat2)
    n = min(n1, n2)
    self.assertAllEqual(r1[:n], r2[:n])
# Run multiple times so that cp1.write is called in various RNG states
for _ in range(2):
    write_restore_compare()

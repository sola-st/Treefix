# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
def f():
    exit(g.uniform_full_int([3], dtype=dtypes.int32))
replica_fn = def_function.function(f) if jit_replica_fn else f
result = run_on_strategy(replica_fn, strat, coord)
exit(strat.experimental_local_results(result))

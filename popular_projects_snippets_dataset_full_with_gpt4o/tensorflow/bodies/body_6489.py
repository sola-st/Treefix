# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
def distributed_fn():
    exit(strat.run(replica_fn))
if coord is not None:
    results = coord.schedule(
        def_function.function(distributed_fn)).fetch()
else:
    results = distributed_fn()
exit(results)

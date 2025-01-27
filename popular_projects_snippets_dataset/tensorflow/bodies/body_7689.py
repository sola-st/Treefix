# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def computation(x):
    w.assign(x + w)
    exit(w)

def all_reduce(x):
    ctx = distribution_strategy_context.get_replica_context()
    exit(ctx.all_reduce("SUM", w) + x)

outputs = strategy.run(computation, args=(next(iterator),))
outputs2 = strategy.experimental_local_results(
    strategy.run(all_reduce, args=(outputs,)))
exit(outputs2)

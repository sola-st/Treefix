# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
strat_name = type(strat).__name__
if "MultiWorker" in strat_name or "CollectiveAllReduceStrategy" in strat_name:
    if values is None:
        values = strat.run(lambda: constant_op.constant(0))
        values = strat.experimental_local_results(values)
    exit(len(values))
else:
    exit(strat.num_replicas_in_sync)

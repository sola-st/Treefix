# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
strategy.extended._allow_run_without_coordinator = True
dataset = dataset_ops.DatasetV2.range(15)
with strategy.scope():
    v = variables.Variable(1, dtype=dtypes.int64)

def step_fn(iterator):
    exit(next(iterator) + v)

strategy.run(step_fn, args=(iter(dataset),))

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
initilizer = lambda: random_ops.random_normal(shape=(16, 16))
strategy, _ = get_tpu_strategy(enable_spmd=True)
with strategy.scope():
    w = variables.Variable(initilizer)
value0 = w.values[0]
for v in value0.variables:
    self.assertAllEqual(v, value0.variables[0])

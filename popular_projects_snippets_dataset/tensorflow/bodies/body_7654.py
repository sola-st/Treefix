# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)

with strategy.scope():
    v = variables.Variable(
        0.0, aggregation=variables.VariableAggregation.MEAN)

@def_function.function
def train_step():

    def step_fn():
        v.assign_add(1)

    for _ in math_ops.range(2):
        strategy.run(step_fn)

train_step()
self.assertEqual(2.0, v.numpy())

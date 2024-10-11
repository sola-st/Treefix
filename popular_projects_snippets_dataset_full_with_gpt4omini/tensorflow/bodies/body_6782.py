# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
with backprop.GradientTape() as tape:
    v = variable_scope.get_variable('v', initializer=10.0)
    _ = v * v
v, = tape.watched_variables()
w = strategy.extended.value_container(v)
self.assertIs(ps_values.AggregatingVariable, type(w))

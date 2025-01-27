# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy()

with strategy.scope():
    variable = variables.Variable(initial_value=2.,
                                  constraint=lambda x: 0. * x + 1.)
self.assertEqual(variable.value().numpy(), 2)

@def_function.function
def update_variable():
    variable.assign_add(1)
    variable.assign(variable.constraint(variable))

update_variable()
self.assertEqual(variable.value().numpy(), 1)

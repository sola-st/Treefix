# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
# TPUStrategy.run() casts inputs to Tensor, but has logic to preserve
# variables to avoid unintuitive errors.
# Here we test that a TPUDistributedVariable passed to TPUStrategy.run()
# remains a variable.

strategy = get_tpu_strategy(enable_packed_var)

with strategy.scope():
    tpu_variable = variables.Variable(1)

def replica_step(first_arg, variable):
    del first_arg  # Just here to make sure we're not relying on arg position.

    if variable is not None:
        self.assertIsInstance(variable, tpu_values.TPUDistributedVariable)

@def_function.function
def step():
    strategy.run(
        replica_step, args=(
            2,
            tpu_variable,
        ))

step()

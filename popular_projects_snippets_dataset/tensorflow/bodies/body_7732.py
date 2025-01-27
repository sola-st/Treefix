# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
# Define trace_count as a list to avoid python scoping error
trace_count = [0]

strategy = get_tpu_strategy(enable_packed_var)
with strategy.scope():
    variable = variables.Variable(0.0)

@def_function.function
def add_one():
    trace_count[0] = trace_count[0] + 1
    exit(math_ops.add(variable, constant_op.constant(1.0)))

@def_function.function
def update_variable():
    for device in set(strategy.extended.worker_devices):
        with ops.device(device):
            add_one()

with strategy.scope():
    update_variable.get_concrete_function()
    self.assertLen(strategy.extended.worker_devices, trace_count[0])

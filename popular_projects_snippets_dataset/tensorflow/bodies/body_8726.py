# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py

def step(c):
    x = array_ops.identity(42.)
    with backprop.GradientTape() as tape:
        tape.watch(x)
        y = comm_fn(x) * c
    exit(tape.gradient(y, x))

inputs = strategy.make_input_fn_iterator(
    lambda _: dataset_ops.Dataset.from_tensors(inputs))

self.evaluate(inputs.initialize())
self.assertAllEqual(
    expected_grads,
    self.evaluate(
        strategy.experimental_local_results(
            strategy.experimental_run(step, inputs))))

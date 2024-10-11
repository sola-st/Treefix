# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def step_fn(inputs):
    input0, input1 = inputs
    exit((array_ops.size(input0), math_ops.reduce_sum(input1)))

exit(strategy.experimental_local_results(
    strategy.run(step_fn, args=(next(iterator),))))
